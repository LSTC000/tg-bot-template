from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.config import settings

from .abc import ABCClient


class PostgresClient(ABCClient):
    @staticmethod
    def get_client() -> async_sessionmaker:
        return async_sessionmaker(
            autocommit=settings.postgres.AUTOCOMMIT,
            autoflush=settings.postgres.AUTOFLUSH,
            bind=create_async_engine(
                echo=settings.postgres.ECHO,
                url=settings.postgres.DSN.unicode_string(),
                pool_pre_ping=settings.postgres.POOL_PRE_PING,
                pool_size=settings.postgres.POOL_SIZE,
                max_overflow=settings.postgres.MAX_OVERFLOW,
            ),
        )


class RedisStorageClient(ABCClient):
    @staticmethod
    def get_client() -> Redis:
        return Redis(
            host=settings.redis.HOST,
            port=settings.redis.PORT,
            db=settings.redis.STORAGE_DB,
            encoding=settings.redis.ENCODING,
            decode_responses=settings.redis.DECODE,
        )


class RedisCacheClient(ABCClient):
    @staticmethod
    def get_client() -> Redis:
        return Redis(
            host=settings.redis.HOST,
            port=settings.redis.PORT,
            db=settings.redis.CACHE_DB,
            encoding=settings.redis.ENCODING,
            decode_responses=settings.redis.DECODE,
        )
