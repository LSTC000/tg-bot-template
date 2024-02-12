from pydantic import Field

from ..core import EnvCoreSettings


class RedisSettings(EnvCoreSettings):
    HOST: str = Field(..., alias="REDIS_HOST", env="REDIS_HOST")
    PORT: int = Field(..., alias="REDIS_PORT", env="REDIS_PORT")

    ENCODING: str = "utf-8"
    DECODE: bool = True

    STORAGE_DB: int = 0
    CACHE_DB: int = 1
