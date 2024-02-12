from abc import ABCMeta, abstractmethod

from src.usecases import UseCaseRepository


class ABCUseCaseDeps(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    async def get() -> UseCaseRepository:
        raise NotImplementedError
