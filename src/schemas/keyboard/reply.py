from pydantic import Field

from ..core import CoreModel


class ReplyKeyboardButton(CoreModel):
    text: str = Field(..., description="Text of keyboard button")


class ReplyKeyboardBuild(CoreModel):
    width: int = Field(8, description="Keyboard width")
    buttons: list[ReplyKeyboardButton] = Field(
        ..., description="Buttons data of keyboard"
    )
