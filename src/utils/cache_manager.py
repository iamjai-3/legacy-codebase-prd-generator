"""
PostgreSQL-based caching system for LLM responses and tool results.

Uses the existing Temporal PostgreSQL database for caching to avoid
additional infrastructure. Supports TTL, automatic cleanup, and multiple cache types.
"""

import asyncio
import hashlib
import json
from collections.abc import Callable
from datetime import datetime, timedelta
from enum import Enum
from functools import wraps
from typing import Any

import asyncpg

from src.config.settings import get_settings
from src.utils.logging_config import get_logger

logger = get_logger(__name__)


class CacheType(str, Enum):
    """Cache entry types."""

    LLM_RESPONSE = "llm_response"
    VECTOR_SEARCH = "vector_search"
    TOOL_RESULT = "tool_result"
    CUSTOM = "custom"


class CacheManager:
    """
    PostgreSQL-based cache manager.

    Features:
    - TTL-based expiration
    - Automatic cleanup
    - Multiple cache types
    - Connection pooling
    - Async support
    """

    def __init__(self):
        """Initialize cache manager."""
        self.settings = get_settings()
        self.cache_settings = self.settings.cache
        self._pool: asyncpg.Pool | None = None
        self._initialized = False

    async def initialize(self):
        """Initialize database connection and create tables."""
        if self._initialized or not self.cache_settings.enabled:
            return

        try:
            # Create connection pool
            self._pool = await asyncpg.create_pool(
                host=self.cache_settings.host,
                port=self.cache_settings.port,
                database=self.cache_settings.database,
                user=self.cache_settings.user,
                password=self.cache_settings.password,
                min_size=2,
                max_size=10,
                command_timeout=60,
            )

            # Create cache table
            await self._create_tables()

            # Start cleanup task
            asyncio.create_task(self._cleanup_loop())

            self._initialized = True
            logger.info("Cache manager initialized successfully")

        except Exception as e:
            logger.error(f"Failed to initialize cache: {e}")
            self.cache_settings.enabled = False

    async def _create_tables(self):
        """Create cache tables if they don't exist."""
        async with self._pool.acquire() as conn:
            await conn.execute(
                """
                CREATE TABLE IF NOT EXISTS prd_agent_cache (
                    cache_key VARCHAR(64) PRIMARY KEY,
                    cache_type VARCHAR(50) NOT NULL,
                    value JSONB NOT NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
                    expires_at TIMESTAMP NOT NULL,
                    hit_count INTEGER DEFAULT 0,
                    metadata JSONB
                );
                
                CREATE INDEX IF NOT EXISTS idx_cache_type ON prd_agent_cache(cache_type);
                CREATE INDEX IF NOT EXISTS idx_expires_at ON prd_agent_cache(expires_at);
            """
            )

    def _generate_key(self, *args, **kwargs) -> str:
        """Generate cache key from arguments."""
        data = json.dumps({"args": args, "kwargs": kwargs}, sort_keys=True)
        return hashlib.sha256(data.encode()).hexdigest()

    async def get(self, key: str, cache_type: CacheType = CacheType.CUSTOM) -> Any | None:
        """
        Get value from cache.

        Args:
            key: Cache key
            cache_type: Type of cache entry

        Returns:
            Cached value or None if not found/expired
        """
        if not self.cache_settings.enabled or not self._initialized:
            return None

        try:
            async with self._pool.acquire() as conn:
                row = await conn.fetchrow(
                    """
                    UPDATE prd_agent_cache
                    SET hit_count = hit_count + 1
                    WHERE cache_key = $1 
                        AND cache_type = $2
                        AND expires_at > NOW()
                    RETURNING value
                """,
                    key,
                    cache_type.value,
                )

                if row:
                    logger.debug(f"Cache hit: {cache_type.value}:{key[:8]}")
                    return row["value"]

                logger.debug(f"Cache miss: {cache_type.value}:{key[:8]}")
                return None

        except Exception as e:
            logger.warning(f"Cache get error: {e}")
            return None

    async def set(
        self,
        key: str,
        value: Any,
        cache_type: CacheType = CacheType.CUSTOM,
        ttl: int | None = None,
        metadata: dict | None = None,
    ):
        """
        Set value in cache.

        Args:
            key: Cache key
            value: Value to cache
            cache_type: Type of cache entry
            ttl: Time to live in seconds (None = use default)
            metadata: Optional metadata
        """
        if not self.cache_settings.enabled or not self._initialized:
            return

        try:
            # Determine TTL
            if ttl is None:
                ttl = {
                    CacheType.LLM_RESPONSE: self.cache_settings.llm_response_ttl,
                    CacheType.VECTOR_SEARCH: self.cache_settings.vector_search_ttl,
                    CacheType.TOOL_RESULT: self.cache_settings.tool_result_ttl,
                }.get(cache_type, 3600)

            expires_at = datetime.now() + timedelta(seconds=ttl)

            async with self._pool.acquire() as conn:
                await conn.execute(
                    """
                    INSERT INTO prd_agent_cache 
                        (cache_key, cache_type, value, expires_at, metadata)
                    VALUES ($1, $2, $3, $4, $5)
                    ON CONFLICT (cache_key) 
                    DO UPDATE SET 
                        value = EXCLUDED.value,
                        expires_at = EXCLUDED.expires_at,
                        metadata = EXCLUDED.metadata
                """,
                    key,
                    cache_type.value,
                    json.dumps(value),
                    expires_at,
                    json.dumps(metadata) if metadata else None,
                )

            logger.debug(f"Cache set: {cache_type.value}:{key[:8]} (ttl={ttl}s)")

        except Exception as e:
            logger.warning(f"Cache set error: {e}")

    async def delete(self, key: str):
        """Delete a cache entry."""
        if not self.cache_settings.enabled or not self._initialized:
            return

        try:
            async with self._pool.acquire() as conn:
                await conn.execute("DELETE FROM prd_agent_cache WHERE cache_key = $1", key)
        except Exception as e:
            logger.warning(f"Cache delete error: {e}")

    async def clear(self, cache_type: CacheType | None = None):
        """
        Clear cache entries.

        Args:
            cache_type: If provided, only clear this type
        """
        if not self.cache_settings.enabled or not self._initialized:
            return

        try:
            async with self._pool.acquire() as conn:
                if cache_type:
                    await conn.execute(
                        "DELETE FROM prd_agent_cache WHERE cache_type = $1", cache_type.value
                    )
                else:
                    await conn.execute("DELETE FROM prd_agent_cache")

            logger.info(f"Cache cleared: {cache_type.value if cache_type else 'all'}")

        except Exception as e:
            logger.warning(f"Cache clear error: {e}")

    async def get_stats(self) -> dict:
        """Get cache statistics."""
        if not self.cache_settings.enabled or not self._initialized:
            return {"enabled": False}

        try:
            async with self._pool.acquire() as conn:
                stats = await conn.fetch(
                    """
                    SELECT 
                        cache_type,
                        COUNT(*) as total_entries,
                        SUM(hit_count) as total_hits,
                        AVG(hit_count) as avg_hits,
                        COUNT(CASE WHEN expires_at > NOW() THEN 1 END) as active_entries
                    FROM prd_agent_cache
                    GROUP BY cache_type
                """
                )

                return {
                    "enabled": True,
                    "by_type": [dict(row) for row in stats],
                }

        except Exception as e:
            logger.warning(f"Cache stats error: {e}")
            return {"enabled": True, "error": str(e)}

    async def _cleanup_expired(self):
        """Remove expired cache entries."""
        if not self.cache_settings.enabled or not self._initialized:
            return

        try:
            async with self._pool.acquire() as conn:
                result = await conn.execute("DELETE FROM prd_agent_cache WHERE expires_at < NOW()")

                # Extract count from result string like "DELETE 5"
                count = int(result.split()[-1]) if result else 0
                if count > 0:
                    logger.info(f"Cleaned up {count} expired cache entries")

        except Exception as e:
            logger.warning(f"Cache cleanup error: {e}")

    async def _cleanup_loop(self):
        """Background task to cleanup expired entries."""
        while True:
            try:
                await asyncio.sleep(self.cache_settings.cleanup_interval)
                await self._cleanup_expired()
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Cleanup loop error: {e}")

    async def close(self):
        """Close cache connections."""
        if self._pool:
            await self._pool.close()
            self._initialized = False


# Global cache instance
_cache_manager: CacheManager | None = None


async def get_cache_manager() -> CacheManager:
    """Get or create global cache manager instance."""
    global _cache_manager

    if _cache_manager is None:
        _cache_manager = CacheManager()
        await _cache_manager.initialize()

    return _cache_manager


def cached(
    cache_type: CacheType = CacheType.CUSTOM,
    ttl: int | None = None,
    key_prefix: str = "",
):
    """
    Decorator for caching function results.

    Example:
        @cached(cache_type=CacheType.LLM_RESPONSE, ttl=3600)
        async def get_llm_response(prompt: str):
            return await llm.generate(prompt)
    """

    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            cache = await get_cache_manager()

            if not cache.cache_settings.enabled:
                return await func(*args, **kwargs)

            # Generate cache key
            key_data = f"{key_prefix}:{func.__name__}:{args}:{kwargs}"
            cache_key = hashlib.sha256(key_data.encode()).hexdigest()

            # Try to get from cache
            cached_value = await cache.get(cache_key, cache_type)
            if cached_value is not None:
                return cached_value

            # Execute function
            result = await func(*args, **kwargs)

            # Store in cache
            await cache.set(
                cache_key, result, cache_type, ttl, metadata={"function": func.__name__}
            )

            return result

        return wrapper

    return decorator
