from abc import ABCMeta, abstractmethod

from aiogram.utils.keyboard import InlineKeyboardMarkup

from src.schemas import InlineKeyboardBuild


class ABCCoreInlineKeyboard(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def builder(build_data: InlineKeyboardBuild) -> InlineKeyboardMarkup:
        raise NotImplementedError


class ABCInlineKeyboardRepository(metaclass=ABCMeta):
    @abstractmethod
    def command(self):
        raise NotImplementedError
