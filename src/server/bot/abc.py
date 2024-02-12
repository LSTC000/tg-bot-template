from abc import ABCMeta, abstractmethod

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage


class ABCServerBot(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    async def init(
        cls, storage: MemoryStorage | RedisStorage
    ) -> tuple[Dispatcher, Bot]:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def run(dp: Dispatcher, bot: Bot) -> None:
        raise NotImplementedError
