from pydantic import Field, PostgresDsn, field_validator
from pydantic_core.core_schema import ValidationInfo

from ..core import EnvCoreSettings


class PostgresSettings(EnvCoreSettings):
    DB: str = Field(..., alias="POSTGRES_DB", env="POSTGRES_DB")
    USER: str = Field(..., alias="POSTGRES_USER", env="POSTGRES_USER")
    PASS: str = Field(..., alias="POSTGRES_PASSWORD", env="POSTGRES_PASSWORD")
    HOST: str = Field(..., alias="POSTGRES_HOST", env="POSTGRES_HOST")
    PORT: int = Field(..., alias="POSTGRES_PORT", env="POSTGRES_PORT")
    TZ: str = Field("Europe/Moscow", env="TZ")

    WEB_CONCURRENCY: int = Field(..., env="WEB_CONCURRENCY")
    MAX_OVERFLOW: int = Field(..., env="MAX_OVERFLOW")
    DB_POOL_SIZE: int = Field(..., env="DB_POOL_SIZE")

    AUTOCOMMIT: bool = False
    AUTOFLUSH: bool = False
    ECHO: bool = False
    POOL_PRE_PING: bool = True

    POOL_SIZE: int | None = None
    DSN: PostgresDsn | None = None

    @field_validator("POOL_SIZE", mode="before")
    def assemble_poll_size(cls, v: int | None, values: ValidationInfo) -> int:
        if isinstance(v, int):
            return v
        return max(
            values.data.get("DB_POOL_SIZE") // values.data.get("WEB_CONCURRENCY"), 5
        )

    @field_validator("DSN", mode="before")
    def assemble_db_connection(
        cls, v: PostgresDsn | None, values: ValidationInfo
    ) -> PostgresDsn:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=values.data.get("USER"),
            password=values.data.get("PASS"),
            host=values.data.get("HOST"),
            port=values.data.get("PORT"),
            path=f'{values.data.get("DB") or ""}',
        )
