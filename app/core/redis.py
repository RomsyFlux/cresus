"""Redis client configuration."""

import redis
from app.core.config import settings


redis_client = redis.from_url(
    settings.REDIS_URL,
    encoding="utf-8",
    decode_responses=True,
)


def get_redis():
    """Get Redis client."""
    return redis_client
