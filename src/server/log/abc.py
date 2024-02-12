from abc import ABCMeta, abstractmethod


class ABCServerLog(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def init(cls) -> None:
        raise NotImplementedError
