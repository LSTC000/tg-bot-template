from aiogram import Bot

from src.common.meta import SingletonMeta
from src.config import settings


class BotLoader(SingletonMeta):
    _tg_token: str = settings.token.TG

    _parse_mode: str = settings.bot.PARSE_MODE
    _disable_web_page_preview: bool = settings.bot.DISABLE_WEB_PAGE_PREVIEW

    @classmethod
    def get_bot(cls) -> Bot:
        return Bot(
            token=cls._tg_token,
            parse_mode=cls._parse_mode,
            disable_web_page_preview=cls._disable_web_page_preview,
        )
