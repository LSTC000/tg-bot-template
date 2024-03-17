from ..core import CoreSettings


class CacheSettings(CoreSettings):
    SERVICE_EXPIRE_SECONDS: int = 60 * 60 * 24
