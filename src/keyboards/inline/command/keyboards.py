from aiogram.utils.keyboard import InlineKeyboardMarkup

from src.config import settings
from src.schemas import InlineKeyboardBuild, InlineKeyboardButton, InlineKeyboardRow

from ..core import CoreInlineKeyboard


class CommandInlineKeyboards(CoreInlineKeyboard):
    _width: str = settings.keyboard.size.WIDTH

    _cmd_start_btn: str = settings.keyboard.button.command.START
    _cmd_start_data: str = settings.keyboard.data.command.START

    def start(self) -> InlineKeyboardMarkup:
        return self.builder(
            build_data=InlineKeyboardBuild(
                width=self._width,
                rows=[
                    InlineKeyboardRow(
                        buttons=[
                            InlineKeyboardButton(
                                text=self._cmd_start_btn,
                                data=self._cmd_start_data,
                            ),
                        ],
                    ),
                ],
            )
        )
