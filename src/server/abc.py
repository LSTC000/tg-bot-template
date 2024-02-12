from abc import ABCMeta, abstractmethod


class ABCServer(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    async def run() -> None:
        raise NotImplementedError
