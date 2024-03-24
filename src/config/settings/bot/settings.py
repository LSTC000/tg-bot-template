from pydantic import Field

from ..core import EnvCoreSettings


class BotSettings(EnvCoreSettings):
    PARSE_MODE: str = "HTML"
    DROP_PENDING_UPDATES: bool = Field(..., env="DROP_PENDING_UPDATES")
    DISABLE_NOTIFICATION: bool = Field(..., env="DISABLE_NOTIFICATION")
    DISABLE_WEB_PAGE_PREVIEW: bool = Field(..., env="DISABLE_WEB_PAGE_PREVIEW")
