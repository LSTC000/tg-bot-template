from abc import ABCMeta, abstractmethod
from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession


class ABCDatabaseDeps(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    async def get() -> AsyncIterator[AsyncSession]:
        raise NotImplementedError
