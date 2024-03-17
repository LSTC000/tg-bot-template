from aiogram import Bot
from loguru import logger

from src.common.logger import LoggerManager
from src.loader import BotLoader


class KeyboardManager:
    _bot: Bot = BotLoader.get_bot()
    _logger: logger = LoggerManager.get_base_logger()

    @classmethod
    async def remove_last_inline_keyboard(
        cls, user_id: int, last_inline_keyboard_message_id: int
    ):
        try:
            await cls._bot.delete_message(
                chat_id=user_id, message_id=last_inline_keyboard_message_id
            )
        except Exception as exc:
            cls._logger.info(f"Error to remove last inline keyboard: {exc}.")

    @classmethod
    async def clear_last_inline_keyboard(
        cls, user_id: int, last_inline_keyboard_message_id: int
    ):
        try:
            await cls._bot.edit_message_reply_markup(
                chat_id=user_id,
                message_id=last_inline_keyboard_message_id,
                reply_markup=None,
            )
        except Exception as exc:
            cls._logger.info(f"Error to clear last inline keyboard: {exc}.")
