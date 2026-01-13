"""
OpenAI Embeddings service for generating vector embeddings.
"""

from langchain_openai import OpenAIEmbeddings
from tenacity import retry, stop_after_attempt, wait_exponential

from src.config.settings import get_settings
from src.utils.logging_config import get_logger

logger = get_logger(__name__)


class EmbeddingService:
    """
    Service for generating embeddings using OpenAI's embedding models.
    Provides caching and batch processing capabilities.
    """

    def __init__(self) -> None:
        """Initialize the embedding service."""
        self.settings = get_settings()
        self._embeddings: OpenAIEmbeddings | None = None

    @property
    def embeddings(self) -> OpenAIEmbeddings:
        """Get or create the OpenAI embeddings instance."""
        if self._embeddings is None:
            self._embeddings = OpenAIEmbeddings(
                model=self.settings.openai.embedding_model,
                openai_api_key=self.settings.openai.api_key,
                dimensions=self.settings.qdrant.vector_size,
            )
            logger.info(
                "Initialized OpenAI embeddings",
                model=self.settings.openai.embedding_model,
                dimensions=self.settings.qdrant.vector_size,
            )
        return self._embeddings

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    async def embed_text(self, text: str) -> list[float]:
        """
        Generate embedding for a single text.

        Args:
            text: Text to embed

        Returns:
            Embedding vector as list of floats
        """
        logger.debug("Generating embedding", text_length=len(text))
        embedding = await self.embeddings.aembed_query(text)
        return embedding

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    async def embed_texts(self, texts: list[str]) -> list[list[float]]:
        """
        Generate embeddings for multiple texts in batch.

        Args:
            texts: List of texts to embed

        Returns:
            List of embedding vectors
        """
        logger.info("Generating batch embeddings", count=len(texts))
        embeddings = await self.embeddings.aembed_documents(texts)
        return embeddings

    def embed_text_sync(self, text: str) -> list[float]:
        """
        Synchronous version of embed_text.

        Args:
            text: Text to embed

        Returns:
            Embedding vector as list of floats
        """
        return self.embeddings.embed_query(text)

    def embed_texts_sync(self, texts: list[str]) -> list[list[float]]:
        """
        Synchronous version of embed_texts.

        Args:
            texts: List of texts to embed

        Returns:
            List of embedding vectors
        """
        return self.embeddings.embed_documents(texts)

    def get_langchain_embeddings(self) -> OpenAIEmbeddings:
        """Get the underlying LangChain embeddings instance for use with vectorstores."""
        return self.embeddings
