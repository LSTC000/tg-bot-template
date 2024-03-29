from typing import Any, Type
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.base import ExecutableOption
from sqlalchemy.sql.elements import BinaryExpression

from src.common.meta import SingletonMeta
from src.config.db import Base


class CoreCRUD[TModel: Base, TCreate: BaseModel, TUpdate: BaseModel](
    metaclass=SingletonMeta
):
    def __init__(self, model: Type[TModel]):
        self.model = model

    async def get(
        self,
        db: AsyncSession,
        sid: UUID,
        custom_options: list[ExecutableOption] | None = None,
    ) -> TModel | None:
        query = select(self.model)

        if custom_options is not None:
            for custom_option in custom_options:
                query = query.options(custom_option)

        query = query.where(self.model.sid == sid)  # noqa

        result: Result = await db.execute(query)
        return result.scalars().first()

    async def get_by(
        self,
        db: AsyncSession,
        query_expression: BinaryExpression,
        custom_options: list[ExecutableOption] | None = None,
    ) -> TModel | None:
        query = select(self.model)

        if custom_options is not None:
            for custom_option in custom_options:
                query = query.options(custom_option)

        query = query.where(query_expression)

        result: Result = await db.execute(query)
        return result.scalars().first()

    async def get_all(
        self,
        db: AsyncSession,
        query_expression: BinaryExpression | None = None,
        custom_options: list[ExecutableOption] | None = None,
    ) -> list[TModel]:
        query = select(self.model)

        if custom_options is not None:
            for custom_option in custom_options:
                query = query.options(custom_option)
        if query_expression is not None:
            query = query.where(query_expression)

        result: Result = await db.execute(query)
        return result.scalars().all()

    async def get_multi(
        self,
        db: AsyncSession,
        offset: int = 0,
        limit: int = 50,
        query_expression: BinaryExpression | None = None,
        custom_options: list[ExecutableOption] | None = None,
    ) -> list[TModel]:
        query = select(self.model)

        if custom_options:
            for custom_option in custom_options:
                query = query.options(custom_option)
        if query_expression is not None:
            query = query.where(query_expression)

        query = query.offset(offset).limit(limit)

        result: Result = await db.execute(query)
        return result.scalars().all()

    async def create(
        self, db: AsyncSession, obj_in: TCreate, with_commit: bool = True
    ) -> TModel:
        obj = self.model(**obj_in.model_dump())

        db.add(obj)

        if with_commit:
            await db.commit()
            await db.refresh(obj)
        else:
            await db.flush()

        return obj

    @staticmethod
    async def update(
        db: AsyncSession,
        obj: TModel,
        obj_in: TUpdate | dict[str, Any],
        with_commit: bool = True,
    ) -> TModel:
        obj_data = obj.__dict__

        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)

        for field in obj_data.keys():
            if field in update_data:
                setattr(obj, field, update_data[field])

        db.add(obj)

        if with_commit:
            await db.commit()
            await db.refresh(obj)
        else:
            await db.flush()

        return obj

    @staticmethod
    async def remove(
        db: AsyncSession, obj: TModel, with_commit: bool = True
    ) -> TModel | None:
        await db.delete(obj)

        if with_commit:
            await db.commit()
        else:
            await db.flush()

        return obj
