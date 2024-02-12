from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage

from src.config.db import RedisStorageClient

from .abc import ABCServerStorage


class ServerStorage(ABCServerStorage):
    @staticmethod
    def get_storage(redis: bool = False) -> MemoryStorage | RedisStorage:
        if redis:
            return RedisStorage(redis=RedisStorageClient.get_client())
        return MemoryStorage()
