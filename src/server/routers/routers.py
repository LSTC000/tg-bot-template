from aiogram import Dispatcher

from src.routers import RoutersRepository

from .abc import ABCServerRouters


class ServerRouters(ABCServerRouters):
    @staticmethod
    def init(dp: Dispatcher) -> None:
        dp.include_routers(RoutersRepository.command)
