from abc import abstractmethod

from src.common.meta import SingletonMeta


class CoreService(metaclass=SingletonMeta):
    @abstractmethod
    def utils(self):
        raise NotImplementedError

    @abstractmethod
    def crud(self):
        raise NotImplementedError


class CoreServiceUtils(metaclass=SingletonMeta):
    pass
