import logging

from src.config.settings import settings

from .abc import ABCServerLog


class ServerLog(ABCServerLog):
    _log_level: str = settings.log.BASE_SERVER_LEVEL
    _log_format: str = settings.log.BASE_SERVER_FORMAT

    @classmethod
    def init(cls) -> None:
        logging.basicConfig(
            level=cls._log_level,
            format=cls._log_format,
        )
