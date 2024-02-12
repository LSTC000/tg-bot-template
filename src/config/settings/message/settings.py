from .abc import ABCMessageSettings
from .command import MessageCommandSettings


class MessageSettings(ABCMessageSettings):
    command: MessageCommandSettings = MessageCommandSettings()
