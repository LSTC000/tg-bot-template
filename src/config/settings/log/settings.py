from ..core import CoreSettings


class LogSettings(CoreSettings):
    BASE_NAME: str = "BOT"
    BASE_LEVEL: str = "INFO"
    BASE_FORMAT: str = "<level>{level}</level> | <blue>{time:YYYY-MM-DD H:M:S}</blue> | <level>{message}</level>"
    BASE_COLORIZE: bool = True

    BASE_SERVER_LEVEL: str = "INFO"
    BASE_SERVER_FORMAT: str = "%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"

    REQUEST_NAME: str = "BOT-REQUEST"
    REQUEST_LEVEL: str = "INFO"
    REQUEST_FORMAT: str = "<level>{level}</level> | <green>{time:YYYY-MM-DD H:M:S}</green> | <level>{message}</level>"
    REQUEST_COLORIZE: bool = True
