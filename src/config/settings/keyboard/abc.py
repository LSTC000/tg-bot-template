from abc import ABCMeta, abstractmethod


class ABCKeyboardSettings(metaclass=ABCMeta):
    @abstractmethod
    def size(self):
        raise NotImplementedError

    @abstractmethod
    def button(self):
        raise NotImplementedError

    @abstractmethod
    def data(self):
        raise NotImplementedError
