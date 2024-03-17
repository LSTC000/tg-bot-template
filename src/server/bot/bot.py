from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage

from src.config.settings import settings
from src.loader import BotLoader

from .abc import ABCServerBot


class ServerBot(ABCServerBot):
    _tg_token: str = settings.token.TG
    _drop_pending_updates: bool = settings.bot.DROP_PENDING_UPDATES

    @classmethod
    async def _init_bot(cls) -> Bot:
        bot = BotLoader.get_bot()
        await bot.delete_webhook(drop_pending_updates=cls._drop_pending_updates)
        return bot

    @classmethod
    async def _init_dp(cls, storage: MemoryStorage | RedisStorage) -> Dispatcher:
        return Dispatcher(storage=storage)

    @classmethod
    async def init(
        cls, storage: MemoryStorage | RedisStorage
    ) -> tuple[Dispatcher, Bot]:
        bot = await cls._init_bot()
        dp = await cls._init_dp(storage=storage)
        return dp, bot

    @staticmethod
    async def run(dp: Dispatcher, bot: Bot) -> None:
        await dp.start_polling(bot)
