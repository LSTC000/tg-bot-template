from .abc import ABCStateSettings
from .command import StateCommandSettings


class StateSettings(ABCStateSettings):
    command: StateCommandSettings = StateCommandSettings()
