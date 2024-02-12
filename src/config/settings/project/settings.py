from pydantic import Field

from ..core import EnvCoreSettings


class ProjectSettings(EnvCoreSettings):
    VERSION: str = Field(..., env="VERSION")
    NAME: str = Field(..., env="NAME")
