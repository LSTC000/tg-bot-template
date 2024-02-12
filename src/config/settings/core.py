from pydantic import Extra
from pydantic_settings import BaseSettings, SettingsConfigDict


class CoreSettings(BaseSettings):
    pass


class EnvCoreSettings(CoreSettings):
    model_config = SettingsConfigDict(env_file=".env", extra=Extra.allow)
