from abc import ABCMeta, abstractmethod


class ABCMessageSettings(metaclass=ABCMeta):
    @abstractmethod
    def command(self):
        raise NotImplementedError
