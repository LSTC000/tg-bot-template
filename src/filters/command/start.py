from aiogram.types import CallbackQuery

from src.config import settings

from ..core import CoreCallbackFilter


class CommandStartFilter(CoreCallbackFilter):
    _cmd_start_clb_data: str = settings.keyboard.data.command.START

    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.data == self._cmd_start_clb_data
