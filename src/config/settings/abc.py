from abc import ABCMeta, abstractmethod


class ABCSettings(metaclass=ABCMeta):
    @abstractmethod
    def bot(self):
        raise NotImplementedError

    @abstractmethod
    def log(self):
        raise NotImplementedError

    @abstractmethod
    def postgres(self):
        raise NotImplementedError

    @abstractmethod
    def project(self):
        raise NotImplementedError

    @abstractmethod
    def redis(self):
        raise NotImplementedError

    @abstractmethod
    def token(self):
        raise NotImplementedError

    @abstractmethod
    def command(self):
        raise NotImplementedError

    @abstractmethod
    def message(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def request(self):
        raise NotImplementedError
