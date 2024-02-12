from abc import ABCMeta, abstractmethod


class ABCStateSettings(metaclass=ABCMeta):
    @abstractmethod
    def command(self):
        raise NotImplementedError
