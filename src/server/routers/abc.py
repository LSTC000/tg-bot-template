from abc import ABCMeta, abstractmethod

from aiogram import Dispatcher


class ABCServerRouters(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def init(dp: Dispatcher) -> None:
        raise NotImplementedError
