from abc import abstractmethod

from src.common.meta import SingletonMeta


class CoreMessage(metaclass=SingletonMeta):
    @abstractmethod
    def services(self):
        raise NotImplementedError

    @abstractmethod
    def keyboards(self):
        raise NotImplementedError
