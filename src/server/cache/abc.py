from abc import ABCMeta, abstractmethod


class ABCServerCache(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def init(cls) -> None:
        raise NotImplementedError
