import sys

from loguru import logger

from src.config import settings


class LoggerManager:
    _base_log_name: str = settings.log.BASE_NAME
    _base_log_level: str = settings.log.BASE_LEVEL
    _base_log_format: str = settings.log.BASE_FORMAT
    _base_log_colorize: bool = settings.log.BASE_COLORIZE

    __request_log_name: str = settings.log.REQUEST_NAME
    __request_log_level: str = settings.log.REQUEST_LEVEL
    __request_log_format: str = settings.log.REQUEST_FORMAT
    __request_log_colorize: bool = settings.log.REQUEST_COLORIZE

    @staticmethod
    def _get_logger(
        log_name: str, log_level: str, log_format: str, log_colorize: bool
    ) -> None:
        logger.remove()
        logger.add(
            sys.stdout,
            level=log_level,
            colorize=log_colorize,
            format=log_format,
            filter=lambda record: record["extra"].get("name") == log_name,
        )

    @classmethod
    def get_base_logger(cls) -> logger:
        cls._get_logger(
            log_name=cls._base_log_name,
            log_level=cls._base_log_level,
            log_format=cls._base_log_format,
            log_colorize=cls._base_log_colorize,
        )
        return logger.bind(name=cls._base_log_name)

    @classmethod
    def get_request_logger(cls) -> logger:
        cls._get_logger(
            log_name=cls.__request_log_name,
            log_level=cls.__request_log_level,
            log_format=cls.__request_log_format,
            log_colorize=cls.__request_log_colorize,
        )
        return logger.bind(name=cls.__request_log_name)
