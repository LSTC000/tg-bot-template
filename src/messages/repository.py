from .abc import ABCMessageRepository
from .command import CommandMessage


class MessageRepository(ABCMessageRepository):
    command: CommandMessage = CommandMessage()
