from abc import ABCMeta, abstractmethod


class ABCKeyboardDataSettings(metaclass=ABCMeta):
    @abstractmethod
    def command(self):
        raise NotImplementedError
