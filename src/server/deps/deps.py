from aiogram import Dispatcher
from aiogram3_di import setup_di

from .abc import ABCServerDeps


class ServerDeps(ABCServerDeps):
    @staticmethod
    def init(dp: Dispatcher) -> None:
        setup_di(dp)
