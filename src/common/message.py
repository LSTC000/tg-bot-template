from aiogram import Bot
from aiogram.types import (
    CallbackQuery,
    ForceReply,
    InlineKeyboardMarkup,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from loguru import logger

from src.common.logger import LoggerManager
from src.config import settings
from src.loader import BotLoader


class MessageManager:
    _bot: Bot = BotLoader.get_bot()
    _logger: logger = LoggerManager.get_base_logger()

    _disable_notification: bool = settings.bot.DISABLE_NOTIFICATION

    @classmethod
    async def send_message(
        cls,
        chat_id: int,
        text: str,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Message:
        try:
            return await cls._bot.send_message(
                chat_id=chat_id,
                text=text,
                reply_markup=reply_markup,
                disable_notification=cls._disable_notification,
            )
        except Exception as exc:
            cls._logger.error(f"Error to send message: {exc}.")

    @classmethod
    async def send_alert(cls, callback: CallbackQuery, text: str) -> None:
        try:
            await callback.answer(
                text=text,
                show_alert=True,
            )
        except Exception as exc:
            cls._logger.error(f"Error to send alert: {exc}.")

    @classmethod
    async def edit_message_reply_markup(
        cls,
        chat_id: int,
        message_id: int,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> None:
        try:
            await cls._bot.edit_message_reply_markup(
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=reply_markup,
            )
        except Exception as exc:
            cls._logger.error(f"Error to edit message reply markup: {exc}.")

    @classmethod
    async def edit_message_text(
        cls,
        chat_id: int,
        message_id: int,
        text: str,
    ) -> None:
        try:
            await cls._bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=text,
            )
        except Exception as exc:
            cls._logger.error(f"Error to edit message text: {exc}.")

    @classmethod
    async def remove_message(
        cls,
        chat_id: int,
        message_id: int,
    ) -> None:
        try:
            await cls._bot.delete_message(
                chat_id=chat_id,
                message_id=message_id,
            )
        except Exception as exc:
            cls._logger.error(f"Error to remove message: {exc}.")
