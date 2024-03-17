from .abc import ABCMessageSettings
from .command import MessageCommandSettings
from .interaction import MessageInteractionSettings


class MessageSettings(ABCMessageSettings):
    command: MessageCommandSettings = MessageCommandSettings()
    interaction: MessageInteractionSettings = MessageInteractionSettings()
