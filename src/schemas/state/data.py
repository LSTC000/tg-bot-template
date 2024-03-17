from pydantic import Field

from ..core import CoreModel


class StateData(CoreModel):
    last_inline_keyboard_message_id: int | None = Field(
        None, description="ID of last inline keyboard message"
    )
