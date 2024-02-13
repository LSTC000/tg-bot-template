from pydantic import Field

from ..core import CoreModel


class ReplyKeyboardButton(CoreModel):
    text: str = Field(..., description="Text of keyboard button")


class ReplyKeyboardRow(CoreModel):
    buttons: list[ReplyKeyboardButton] = Field(
        ..., description="Buttons data of keyboard"
    )


class ReplyKeyboardBuild(CoreModel):
    width: int = Field(8, description="Keyboard width")
    rows: list[ReplyKeyboardRow] = Field(..., description="Rows of keyboard")
