from abc import ABCMeta, abstractmethod

from aiogram import Dispatcher


class ABCServerDeps(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    async def init(dp: Dispatcher) -> None:
        raise NotImplementedError
