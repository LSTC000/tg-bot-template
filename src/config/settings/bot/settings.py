from pydantic import Field

from ..core import EnvCoreSettings


class BotSettings(EnvCoreSettings):
    DROP_PENDING_UPDATES: str = Field(..., env="DROP_PENDING_UPDATES")
