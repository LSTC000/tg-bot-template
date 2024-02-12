from abc import ABCMeta, abstractmethod


class ABCServiceRepository(metaclass=ABCMeta):
    @abstractmethod
    def command(self):
        raise NotImplementedError
