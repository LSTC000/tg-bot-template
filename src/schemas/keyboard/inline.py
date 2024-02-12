from pydantic import Field

from ..core import CoreModel


class InlineKeyboardButton(CoreModel):
    text: str = Field(..., description="Text of keyboard button")
    data: str | None = Field(None, description="Callback data of keyboard button")
    url: str | None = Field(None, description="URL of keyboard button")


class InlineKeyboardBuild(CoreModel):
    width: int = Field(8, description="Keyboard width")
    buttons: list[InlineKeyboardButton] = Field(
        ..., description="Buttons data of keyboard"
    )
