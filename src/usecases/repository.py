from .abc import ABCUseCaseRepository
from .command import CommandUseCase


class UseCaseRepository(ABCUseCaseRepository):
    command: CommandUseCase = CommandUseCase()
