from pydantic import Field

from ..core import CoreSettings


class BaseCommand(CoreSettings):
    name: str = Field(..., description="Name of command")
    description: str = Field(..., description="Description of command")


class CommandSettings(CoreSettings):
    START: BaseCommand = BaseCommand(
        name="/start",
        description="Начать работу",
    )
