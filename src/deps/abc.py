from abc import ABCMeta, abstractmethod


class ABCDepsRepository(metaclass=ABCMeta):
    @abstractmethod
    def db(self):
        raise NotImplementedError

    @abstractmethod
    def use_case(self):
        raise NotImplementedError
