from abc import ABCMeta, abstractmethod


class ABCKeyboardButtonSettings(metaclass=ABCMeta):
    @abstractmethod
    def command(self):
        raise NotImplementedError
