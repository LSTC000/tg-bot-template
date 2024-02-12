from abc import ABCMeta, abstractmethod


class ABCCRUDRepository(metaclass=ABCMeta):
    @abstractmethod
    def user(self):
        raise NotImplementedError
