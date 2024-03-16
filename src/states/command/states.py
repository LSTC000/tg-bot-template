from aiogram.fsm.state import State

from ..core import CoreStatesGroup


class CommandStatesGroup(CoreStatesGroup):
    START = State()
