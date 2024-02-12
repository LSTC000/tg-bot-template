from .abc import ABCKeyboardRepository
from .inline import InlineKeyboardRepository
from .reply import ReplyKeyboardRepository


class KeyboardRepository(ABCKeyboardRepository):
    inline: InlineKeyboardRepository = InlineKeyboardRepository()
    reply: ReplyKeyboardRepository = ReplyKeyboardRepository()
