"""
Application settings and configuration management using Pydantic Settings.
"""

from enum import Enum
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# Load .env file at module import time
_env_file = Path(__file__).parent.parent.parent / ".env"
if _env_file.exists():
    load_dotenv(_env_file)


class LLMProvider(str, Enum):
    """Supported LLM providers."""

    OPENAI = "openai"
    ANTHROPIC = "anthropic"


class EmbeddingProvider(str, Enum):
    """Supported embedding providers."""

    OPENAI = "openai"
    # Add more providers as needed (e.g., VOYAGE, COHERE)


class OpenAISettings(BaseSettings):
    """OpenAI API configuration."""

    model_config = SettingsConfigDict(env_prefix="OPENAI_", extra="ignore")

    api_key: str = Field(default="", description="OpenAI API key")
    model: str = Field(default="gpt-4o", description="Model for chat completions")
    embedding_model: str = Field(
        default="text-embedding-3-large", description="Model for embeddings"
    )
    max_tokens: int = Field(default=4096, description="Max tokens for completions")
    temperature: float = Field(default=0.1, description="Temperature for completions")


class AnthropicSettings(BaseSettings):
    """Anthropic API configuration."""

    model_config = SettingsConfigDict(env_prefix="ANTHROPIC_", extra="ignore")

    api_key: str = Field(default="", description="Anthropic API key")
    model: str = Field(
        default="claude-sonnet-4-5-20250929", description="Model for chat completions"
    )
    max_tokens: int = Field(default=4096, description="Max tokens for completions")
    temperature: float = Field(default=0.1, description="Temperature for completions")


class LLMSettings(BaseSettings):
    """LLM provider selection settings."""

    model_config = SettingsConfigDict(extra="ignore")

    provider: LLMProvider = Field(
        default=LLMProvider.OPENAI,
        description="LLM provider to use (openai or anthropic)",
        validation_alias="LLM_PROVIDER",
    )
    embedding_provider: EmbeddingProvider = Field(
        default=EmbeddingProvider.OPENAI,
        description="Embedding provider to use",
        validation_alias="EMBEDDING_PROVIDER",
    )


class QdrantSettings(BaseSettings):
    """Qdrant vector database configuration."""

    model_config = SettingsConfigDict(env_prefix="QDRANT_", extra="ignore")

    host: str = Field(default="localhost", description="Qdrant host")
    port: int = Field(default=6333, description="Qdrant port")
    api_key: str | None = Field(default=None, description="Qdrant API key")
    collection_prefix: str = Field(default="prd_agent", description="Prefix for collection names")
    vector_size: int = Field(default=1536, description="Vector dimension size")


class TemporalSettings(BaseSettings):
    """Temporal workflow orchestration configuration."""

    model_config = SettingsConfigDict(env_prefix="TEMPORAL_", extra="ignore")

    host: str = Field(default="localhost", description="Temporal host")
    port: int = Field(default=7233, description="Temporal port")
    namespace: str = Field(default="default", description="Temporal namespace")
    task_queue: str = Field(default="prd-agent-queue", description="Task queue name")

    @property
    def address(self) -> str:
        """Get the full Temporal address."""
        return f"{self.host}:{self.port}"


class MinioSettings(BaseSettings):
    """Minio object storage configuration."""

    model_config = SettingsConfigDict(env_prefix="MINIO_", extra="ignore")

    endpoint: str = Field(default="localhost:9000", description="Minio endpoint")
    access_key: str = Field(default="minioadmin", description="Minio access key")
    secret_key: str = Field(default="minioadmin", description="Minio secret key")
    bucket: str = Field(default="metadatas", description="Default bucket name")
    secure: bool = Field(default=False, description="Use HTTPS")


class CacheSettings(BaseSettings):
    """PostgreSQL cache configuration."""

    model_config = SettingsConfigDict(env_prefix="CACHE_", extra="ignore")

    enabled: bool = Field(default=True, description="Enable caching")
    host: str = Field(default="localhost", description="PostgreSQL host")
    port: int = Field(default=5432, description="PostgreSQL port")
    database: str = Field(default="temporal", description="Database name")
    user: str = Field(default="temporal", description="Database user")
    password: str = Field(default="temporal", description="Database password")

    # Cache TTL settings (in seconds)
    llm_response_ttl: int = Field(default=86400, description="LLM response cache TTL (1 day)")
    vector_search_ttl: int = Field(default=3600, description="Vector search cache TTL (1 hour)")
    tool_result_ttl: int = Field(default=1800, description="Tool result cache TTL (30 min)")

    # Cache behavior
    max_cache_size_mb: int = Field(default=500, description="Max cache size in MB")
    cleanup_interval: int = Field(default=3600, description="Cleanup interval in seconds")


class Settings(BaseSettings):
    """Main application settings aggregating all configuration."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # Sub-configurations
    llm: LLMSettings = Field(default_factory=LLMSettings)
    openai: OpenAISettings = Field(default_factory=OpenAISettings)
    anthropic: AnthropicSettings = Field(default_factory=AnthropicSettings)
    qdrant: QdrantSettings = Field(default_factory=QdrantSettings)
    temporal: TemporalSettings = Field(default_factory=TemporalSettings)
    minio: MinioSettings = Field(default_factory=MinioSettings)
    cache: CacheSettings = Field(default_factory=CacheSettings)

    # Application settings
    log_level: str = Field(default="INFO", description="Logging level")
    debug: bool = Field(default=False, description="Debug mode")
    chunk_size: int = Field(default=1000, description="Text chunk size for splitting")
    chunk_overlap: int = Field(default=200, description="Overlap between chunks")
    max_retries: int = Field(default=3, description="Max retries for operations")
    prd_context_max_chars: int = Field(
        default=2000,
        description="Max characters per context chunk included in PRD prompts",
        validation_alias="PRD_CONTEXT_MAX_CHARS",
    )

    # Paths
    uploads_dir: str = Field(default="./uploads", description="Upload directory")
    output_dir: str = Field(default="./output", description="Output directory")


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
