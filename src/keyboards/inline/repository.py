from .abc import ABCInlineKeyboardRepository
from .command import CommandInlineKeyboards


class InlineKeyboardRepository(ABCInlineKeyboardRepository):
    command: CommandInlineKeyboards = CommandInlineKeyboards()
