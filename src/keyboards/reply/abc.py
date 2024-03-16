from abc import ABCMeta, abstractmethod

from aiogram.utils.keyboard import ReplyKeyboardMarkup

from src.schemas import ReplyKeyboardBuild


class ABCCoreReplyKeyboard(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def builder(build_data: ReplyKeyboardBuild) -> ReplyKeyboardMarkup:
        raise NotImplementedError


class ABCReplyKeyboardRepository(metaclass=ABCMeta):  # noqa: B024
    ...
