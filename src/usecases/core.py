from abc import abstractmethod

from src.common.meta import SingletonMeta


class CoreUseCase(metaclass=SingletonMeta):
    @abstractmethod
    def services(self):
        raise NotImplementedError

    @abstractmethod
    def keyboards(self):
        raise NotImplementedError
