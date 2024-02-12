from pydantic import Field

from ..core import EnvCoreSettings


class TokenSettings(EnvCoreSettings):
    TG: str = Field(..., alias="TG_TOKEN", env="TG_TOKEN")
