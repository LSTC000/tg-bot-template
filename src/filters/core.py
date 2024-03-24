from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery, Message


class CoreMessageFilter(BaseFilter):
    def __init__(self):
        ...

    async def __call__(self, message: Message) -> bool:
        ...


class CoreCallbackFilter(BaseFilter):
    def __init__(self):
        ...

    async def __call__(self, callback: CallbackQuery) -> bool:
        ...
