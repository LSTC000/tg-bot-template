from abc import ABCMeta, abstractmethod
from typing import Any


class ABCClient(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def get_client() -> Any:
        raise NotImplementedError
