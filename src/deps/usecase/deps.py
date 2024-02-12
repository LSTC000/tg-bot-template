from src.usecases import UseCaseRepository

from .abc import ABCUseCaseDeps


class UseCaseDeps(ABCUseCaseDeps):
    @staticmethod
    async def get() -> UseCaseRepository:
        return UseCaseRepository()
