from abc import ABCMeta, abstractmethod


class ABCMessageRepository(metaclass=ABCMeta):
    @abstractmethod
    def command(self):
        raise NotImplementedError
