from functools import lru_cache

from .abc import ABCSettings
from .bot import BotSettings
from .command import CommandSettings
from .keyboard import KeyboardSettings
from .log import LogSettings
from .message import MessageSettings
from .postgres import PostgresSettings
from .project import ProjectSettings
from .redis import RedisSettings
from .request import RequestSettings
from .state import StateSettings
from .token import TokenSettings


class Settings(ABCSettings):
    log: LogSettings = LogSettings()
    bot: BotSettings = BotSettings()
    postgres: PostgresSettings = PostgresSettings()
    project: ProjectSettings = ProjectSettings()
    redis: RedisSettings = RedisSettings()
    token: TokenSettings = TokenSettings()
    command: CommandSettings = CommandSettings()
    message: MessageSettings = MessageSettings()
    keyboard: KeyboardSettings = KeyboardSettings()
    state: StateSettings = StateSettings()
    request: RequestSettings = RequestSettings()


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()
