from abc import ABCMeta, abstractmethod


class ABCUseCaseRepository(metaclass=ABCMeta):
    @abstractmethod
    def command(self):
        raise NotImplementedError
