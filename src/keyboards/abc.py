from abc import ABCMeta, abstractmethod


class ABCKeyboardRepository(metaclass=ABCMeta):
    @abstractmethod
    def inline(self):
        raise NotImplementedError

    @abstractmethod
    def reply(self):
        raise NotImplementedError
