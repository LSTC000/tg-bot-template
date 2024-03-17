from aiogram import Bot

from src.common.meta import SingletonMeta
from src.config import settings


class BotLoader(SingletonMeta):
    _tg_token: str = settings.token.TG

    @classmethod
    def get_bot(cls) -> Bot:
        return Bot(token=cls._tg_token)
