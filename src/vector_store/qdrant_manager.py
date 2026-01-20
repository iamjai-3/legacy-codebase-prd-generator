"""
Qdrant Vector Store Manager for knowledge base operations.
"""

from dataclasses import dataclass
from typing import Any
from uuid import uuid4

from langchain_core.documents import Document
from langchain_qdrant import QdrantVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from qdrant_client import QdrantClient, models
from qdrant_client.http.exceptions import UnexpectedResponse

from src.config.settings import get_settings
from src.utils.logging_config import get_logger
from src.vector_store.embeddings import EmbeddingService

logger = get_logger(__name__)


@dataclass
class SearchResult:
    """Represents a search result from the vector store."""

    content: str
    metadata: dict[str, Any]
    score: float
    document_id: str


class QdrantManager:
    """
    Manager class for Qdrant vector database operations.
    Handles collection creation, document storage, and semantic search.
    """

    def __init__(self) -> None:
        """Initialize the Qdrant manager."""
        self.settings = get_settings()
        self.embedding_service = EmbeddingService()
        self._client: QdrantClient | None = None
        self._text_splitter: RecursiveCharacterTextSplitter | None = None

    @property
    def client(self) -> QdrantClient:
        """Get or create the Qdrant client."""
        if self._client is None:
            # Use HTTP for localhost, HTTPS for remote
            use_https = self.settings.qdrant.host not in ("localhost", "127.0.0.1")
            protocol = "https" if use_https else "http"
            url = f"{protocol}://{self.settings.qdrant.host}:{self.settings.qdrant.port}"

            # Only use API key for remote/HTTPS connections
            client_kwargs = {"url": url}
            if use_https and self.settings.qdrant.api_key:
                client_kwargs["api_key"] = self.settings.qdrant.api_key

            self._client = QdrantClient(**client_kwargs)
            logger.info(
                "Connected to Qdrant",
                url=url,
                host=self.settings.qdrant.host,
                port=self.settings.qdrant.port,
            )
        return self._client

    @property
    def text_splitter(self) -> RecursiveCharacterTextSplitter:
        """Get the text splitter instance."""
        if self._text_splitter is None:
            self._text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=self.settings.chunk_size,
                chunk_overlap=self.settings.chunk_overlap,
                length_function=len,
                separators=["\n\n", "\n", " ", ""],
            )
        return self._text_splitter

    def get_collection_name(self, form_name: str) -> str:
        """
        Generate a collection name for a form.

        Args:
            form_name: Name of the form (e.g., 'le01', 'ea01')

        Returns:
            Full collection name with prefix
        """
        # Sanitize form name
        sanitized = form_name.lower().replace(" ", "_").replace("-", "_")
        return f"{self.settings.qdrant.collection_prefix}_{sanitized}"

    def create_collection(self, form_name: str, recreate: bool = False) -> str:
        """
        Create a Qdrant collection for a form.

        Args:
            form_name: Name of the form
            recreate: If True, delete existing collection first

        Returns:
            Collection name
        """
        collection_name = self.get_collection_name(form_name)

        try:
            # Check if collection exists
            collections = self.client.get_collections().collections
            exists = any(c.name == collection_name for c in collections)

            if exists:
                if recreate:
                    logger.info("Deleting existing collection", collection=collection_name)
                    self.client.delete_collection(collection_name)
                else:
                    logger.info("Collection already exists", collection=collection_name)
                    return collection_name

            # Create collection with OpenAI embedding dimensions
            self.client.create_collection(
                collection_name=collection_name,
                vectors_config=models.VectorParams(
                    size=self.settings.qdrant.vector_size,
                    distance=models.Distance.COSINE,
                ),
                optimizers_config=models.OptimizersConfigDiff(
                    indexing_threshold=0,  # Index immediately
                ),
            )

            logger.info(
                "Created collection",
                collection=collection_name,
                vector_size=self.settings.qdrant.vector_size,
            )

        except UnexpectedResponse as e:
            logger.error("Failed to create collection", error=str(e))
            raise

        return collection_name

    def add_documents(
        self, form_name: str, documents: list[Document], batch_size: int = 100
    ) -> int:
        """
        Add documents to the collection with chunking and embedding.

        Args:
            form_name: Name of the form/collection
            documents: List of LangChain Documents to add
            batch_size: Number of documents to process at once

        Returns:
            Number of chunks added
        """
        collection_name = self.get_collection_name(form_name)

        # Ensure collection exists
        self.create_collection(form_name, recreate=False)

        # Split documents into chunks
        all_chunks: list[Document] = []
        for doc in documents:
            chunks = self.text_splitter.split_documents([doc])
            all_chunks.extend(chunks)

        logger.info(
            "Split documents into chunks", original_docs=len(documents), chunks=len(all_chunks)
        )

        # Process in batches
        total_added = 0
        for i in range(0, len(all_chunks), batch_size):
            batch = all_chunks[i : i + batch_size]

            # Generate embeddings
            texts = [chunk.page_content for chunk in batch]
            embeddings = self.embedding_service.embed_texts_sync(texts)

            # Create points for Qdrant
            points = [
                models.PointStruct(
                    id=str(uuid4()),
                    vector=embedding,
                    payload={
                        "content": chunk.page_content,
                        "metadata": chunk.metadata,
                        "form_name": form_name,
                    },
                )
                for chunk, embedding in zip(batch, embeddings)
            ]

            # Upsert to Qdrant
            self.client.upsert(
                collection_name=collection_name,
                points=points,
            )

            total_added += len(points)
            logger.debug("Added batch to collection", batch_size=len(points), total=total_added)

        logger.info(
            "Finished adding documents", collection=collection_name, total_chunks=total_added
        )

        return total_added

    def add_text(
        self,
        form_name: str,
        text: str,
        metadata: dict[str, Any] | None = None,
        doc_type: str = "general",
    ) -> int:
        """
        Add a single text to the collection.

        Args:
            form_name: Name of the form/collection
            text: Text content to add
            metadata: Optional metadata
            doc_type: Type of document (e.g., 'code', 'screenshot', 'jira')

        Returns:
            Number of chunks added
        """
        doc_metadata = metadata or {}
        doc_metadata["doc_type"] = doc_type

        document = Document(page_content=text, metadata=doc_metadata)
        return self.add_documents(form_name, [document])

    def search(
        self,
        form_name: str,
        query: str,
        limit: int = 10,
        score_threshold: float = 0.5,
        filter_metadata: dict[str, Any] | None = None,
    ) -> list[SearchResult]:
        """
        Perform semantic search in a collection.

        Args:
            form_name: Name of the form/collection
            query: Search query
            limit: Maximum number of results
            score_threshold: Minimum similarity score
            filter_metadata: Optional metadata filter

        Returns:
            List of search results
        """
        collection_name = self.get_collection_name(form_name)

        # Generate query embedding
        query_embedding = self.embedding_service.embed_text_sync(query)

        # Build filter if provided
        query_filter = None
        if filter_metadata:
            conditions = []
            for key, value in filter_metadata.items():
                # Support both direct metadata keys and nested metadata keys
                if key == "doc_type" or key == "chunk_type":
                    # These are stored in metadata.doc_type or metadata.chunk_type
                    conditions.append(
                        models.FieldCondition(
                            key=f"metadata.{key}", 
                            match=models.MatchValue(value=value)
                        )
                    )
                else:
                    # Other metadata fields
                    conditions.append(
                        models.FieldCondition(
                            key=f"metadata.{key}", 
                            match=models.MatchValue(value=value)
                        )
                    )
            if conditions:
                query_filter = models.Filter(must=conditions)

        # Perform search using query_points (newer API)
        # query_points accepts query as a list of floats (the embedding vector)
        query_response = self.client.query_points(
            collection_name=collection_name,
            query=query_embedding,  # Direct vector as list of floats
            limit=limit,
            score_threshold=score_threshold,
            query_filter=query_filter,
            with_payload=True,
            with_vectors=False,
        )
        # Extract the points from the QueryResponse
        results = query_response.points if hasattr(query_response, "points") else []

        # Convert to SearchResult objects
        # query_points returns ScoredPoint objects with id, score, and payload
        search_results = []
        for point in results:
            # Extract data from ScoredPoint
            payload = point.payload if hasattr(point, "payload") else {}
            score = point.score if hasattr(point, "score") else 0.0
            point_id = point.id if hasattr(point, "id") else None

            # Handle payload - it should be a dict
            if not isinstance(payload, dict):
                payload = {}

            search_results.append(
                SearchResult(
                    content=payload.get("content", ""),
                    metadata=payload.get("metadata", {}),
                    score=float(score) if score else 0.0,
                    document_id=str(point_id) if point_id else "",
                )
            )

        logger.info(
            "Search completed",
            collection=collection_name,
            query_length=len(query),
            results=len(search_results),
        )

        return search_results

    def get_vector_store(self, form_name: str) -> QdrantVectorStore:
        """
        Get a LangChain QdrantVectorStore instance for a collection.

        Args:
            form_name: Name of the form/collection

        Returns:
            QdrantVectorStore instance for use with LangChain
        """
        collection_name = self.get_collection_name(form_name)

        return QdrantVectorStore(
            client=self.client,
            collection_name=collection_name,
            embedding=self.embedding_service.get_langchain_embeddings(),
        )

    def get_collection_stats(self, form_name: str) -> dict[str, Any]:
        """
        Get statistics for a collection.

        Args:
            form_name: Name of the form/collection

        Returns:
            Dictionary with collection statistics
        """
        collection_name = self.get_collection_name(form_name)

        try:
            info = self.client.get_collection(collection_name)
            # Handle status - it can be a string or an object with .value
            status_value = info.status
            if hasattr(status_value, "value"):
                status_value = status_value.value

            return {
                "name": collection_name,
                "exists": True,
                "vectors_count": getattr(info, "indexed_vectors_count", info.points_count) or 0,
                "points_count": info.points_count or 0,
                "status": str(status_value),
                "optimizer_status": str(info.optimizer_status),
            }
        except UnexpectedResponse:
            return {"name": collection_name, "exists": False}

    def delete_collection(self, form_name: str) -> bool:
        """
        Delete a collection.

        Args:
            form_name: Name of the form/collection

        Returns:
            True if deleted successfully
        """
        collection_name = self.get_collection_name(form_name)

        try:
            self.client.delete_collection(collection_name)
            logger.info("Deleted collection", collection=collection_name)
            return True
        except UnexpectedResponse as e:
            logger.error("Failed to delete collection", error=str(e))
            return False

    def list_collections(self) -> list[str]:
        """List all collections with the agent prefix."""
        collections = self.client.get_collections().collections
        prefix = self.settings.qdrant.collection_prefix
        return [c.name for c in collections if c.name.startswith(prefix)]
