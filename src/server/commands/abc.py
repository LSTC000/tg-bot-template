from abc import ABCMeta, abstractmethod

from aiogram import Bot


class ABCServerCommands(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    async def init(cls, bot: Bot) -> None:
        raise NotImplementedError
