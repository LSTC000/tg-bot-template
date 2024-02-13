from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup

from src.schemas import ReplyKeyboardBuild

from .abc import ABCCoreReplyKeyboard


class CoreReplyKeyboard(ABCCoreReplyKeyboard):
    @staticmethod
    def builder(build_data: ReplyKeyboardBuild) -> ReplyKeyboardMarkup:
        bldr: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

        for row in build_data.rows:
            buttons: list[KeyboardButton] = []
            for button in row.buttons:
                buttons.append(
                    KeyboardButton(
                        text=button.text,
                    )
                )

            bldr.row(*buttons, width=build_data.width)

        return bldr.as_markup()
