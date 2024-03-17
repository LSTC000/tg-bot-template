from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from src.config.db import RedisCacheClient

from .abc import ABCServerCache


class ServerCache(ABCServerCache):
    @classmethod
    def init(cls) -> None:
        FastAPICache.init(
            RedisBackend(RedisCacheClient.get_client()), prefix="bot-cache"
        )
