from .abc import ABCKeyboardSettings
from .button import KeyboardButtonSettings
from .data import KeyboardDataSettings
from .size import KeyboardSizeSettings


class KeyboardSettings(ABCKeyboardSettings):
    size: KeyboardSizeSettings = KeyboardSizeSettings()
    button: KeyboardButtonSettings = KeyboardButtonSettings()
    data: KeyboardDataSettings = KeyboardDataSettings()
