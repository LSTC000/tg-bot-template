from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession

from src.config.db import PostgresClient

from .abc import ABCDatabaseDeps


class DatabaseDeps(ABCDatabaseDeps):
    @staticmethod
    async def get() -> AsyncIterator[AsyncSession]:
        db = PostgresClient.get_client()()
        try:
            yield db
        finally:
            await db.close()
