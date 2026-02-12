"""
Embeddings service for generating vector embeddings.

Supports multiple embedding providers configurable via environment variables.
Currently supports:
- OpenAI (default)
- Additional providers can be added as needed
"""

from langchain_core.embeddings import Embeddings
from langchain_openai import OpenAIEmbeddings
from tenacity import retry, stop_after_attempt, wait_exponential

from src.config.settings import get_settings
from src.utils.logging_config import get_logger

logger = get_logger(__name__)


class EmbeddingService:
    """
    Service for generating embeddings using configurable embedding providers.

    Provider selection is controlled via EMBEDDING_PROVIDER environment variable.
    Currently supports OpenAI embeddings. Additional providers can be added.

    Note: Anthropic does not provide embedding models directly. When using
    Anthropic as the LLM provider, embeddings will still use OpenAI or
    another supported embedding provider.
    """

    def __init__(self) -> None:
        """Initialize the embedding service."""
        self.settings = get_settings()
        self._embeddings: Embeddings | None = None

    @property
    def embeddings(self) -> Embeddings:
        """Get or create the embeddings instance based on configured provider."""
        if self._embeddings is None:
            self._embeddings = self._create_embeddings()
        return self._embeddings

    def _create_embeddings(self) -> Embeddings:
        """
        Create the embeddings instance.

        Currently only OpenAI is supported. Additional providers can be added
        by branching on self.settings.llm.embedding_provider.

        Returns:
            Embeddings instance
        """
        embeddings = OpenAIEmbeddings(
            model=self.settings.openai.embedding_model,
            openai_api_key=self.settings.openai.api_key,
            dimensions=self.settings.qdrant.vector_size,
        )
        logger.info(
            "Initialized OpenAI embeddings",
            provider="openai",
            model=self.settings.openai.embedding_model,
            dimensions=self.settings.qdrant.vector_size,
        )
        return embeddings

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

    def get_langchain_embeddings(self) -> Embeddings:
        """Get the underlying LangChain embeddings instance for use with vectorstores."""
        return self.embeddings
