from .abc import ABCKeyboardButtonSettings
from .command import KeyboardButtonCommandSettings


class KeyboardButtonSettings(ABCKeyboardButtonSettings):
    command: KeyboardButtonCommandSettings = KeyboardButtonCommandSettings()
