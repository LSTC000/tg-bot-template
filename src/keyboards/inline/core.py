from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from src.schemas import InlineKeyboardBuild

from .abc import ABCCoreInlineKeyboard


class CoreInlineKeyboard(ABCCoreInlineKeyboard):
    @staticmethod
    def builder(build_data: InlineKeyboardBuild) -> InlineKeyboardMarkup:
        bldr: InlineKeyboardBuilder = InlineKeyboardBuilder()

        for row in build_data.rows:
            buttons: list[InlineKeyboardButton] = []
            for button in row.buttons:
                buttons.append(
                    InlineKeyboardButton(
                        text=button.text,
                        url=button.url,
                        callback_data=button.data,
                    )
                )

            bldr.row(*buttons, width=build_data.width)

        return bldr.as_markup()
