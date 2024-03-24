from aiogram.types import InlineKeyboardMarkup
from loguru import logger

from src.common.logger import LoggerManager

from .message import MessageManager


class KeyboardManager:
    _logger: logger = LoggerManager.get_base_logger()

    @classmethod
    async def remove_last_inline_keyboard(
        cls, user_id: int, last_inline_keyboard_message_id: int
    ) -> None:
        try:
            await MessageManager.delete_message(
                chat_id=user_id, message_id=last_inline_keyboard_message_id
            )
        except Exception as exc:
            cls._logger.error(f"Error to remove last inline keyboard: {exc}.")

    @classmethod
    async def clear_last_inline_keyboard(
        cls, user_id: int, last_inline_keyboard_message_id: int
    ) -> None:
        try:
            await MessageManager.edit_message_reply_markup(
                chat_id=user_id,
                message_id=last_inline_keyboard_message_id,
                reply_markup=None,
            )
        except Exception as exc:
            cls._logger.error(f"Error to clear last inline keyboard: {exc}.")

    @classmethod
    async def change_last_inline_keyboard(
        cls,
        user_id: int,
        last_inline_keyboard_message_id: int,
        new_last_inline_keyboard: InlineKeyboardMarkup,
    ) -> None:
        try:
            await MessageManager.edit_message_reply_markup(
                chat_id=user_id,
                message_id=last_inline_keyboard_message_id,
                reply_markup=new_last_inline_keyboard,
            )
        except Exception as exc:
            cls._logger.error(f"Error to change last inline keyboard: {exc}.")
