from aiogram.filters import BaseFilter


class CoreFilter(BaseFilter):
    def __init__(self):
        ...

    async def __call__(self) -> bool:
        ...
