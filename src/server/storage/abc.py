from abc import ABCMeta, abstractmethod

from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage


class ABCServerStorage(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def get_storage(redis: bool = False) -> MemoryStorage | RedisStorage:
        raise NotImplementedError
