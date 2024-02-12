from .abc import ABCKeyboardDataSettings
from .command import KeyboardDataCommandSettings


class KeyboardDataSettings(ABCKeyboardDataSettings):
    command: KeyboardDataCommandSettings = KeyboardDataCommandSettings()
