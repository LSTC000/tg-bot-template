from .abc import ABCServiceRepository
from .command import CommandService


class ServiceRepository(ABCServiceRepository):
    command: CommandService = CommandService()
