import hashlib
import json
from typing import Any

from fastapi_cache import Coder, FastAPICache
from fastapi_cache.coder import JsonEncoder, object_hook
from starlette.responses import JSONResponse

from src.config import settings


class CacheManager:
    _service_expire: int = settings.cache.SERVICE_EXPIRE_SECONDS

    class ServiceCoder(Coder):
        @classmethod
        def encode(cls, value: Any) -> str:
            if isinstance(value, JSONResponse):
                return value.body
            return json.dumps(value, cls=JsonEncoder)

        @classmethod
        def decode(cls, value: str) -> dict | str:
            class CustomDict(dict):
                def __init__(self, *args, **kwargs):
                    super(CustomDict, self).__init__(*args, **kwargs)
                    self.__dict__ = self

            if value.isdigit():
                return value

            custom_dict = CustomDict()
            custom_dict.update(json.loads(value, object_hook=object_hook))

            return custom_dict

    @staticmethod
    def _service_key_builder(
        func,
        namespace: str = "",
        *args,
        **kwargs,
    ) -> str:
        prefix = f"{FastAPICache.get_prefix()}:{namespace}:"

        kwargs = kwargs["kwargs"]
        if "db" in kwargs.keys():
            kwargs.pop("db")

        return (
            prefix
            + hashlib.md5(
                f"{func.__module__}:{func.__name__}:{kwargs}".encode()
            ).hexdigest()
        )

    @classmethod
    def service(cls, expire: int | None = None, service_coder: bool = True) -> dict:
        options = {
            "expire": expire if expire else cls._service_expire,
            "key_builder": cls._service_key_builder,
        }

        if service_coder:
            options["coder"] = cls.ServiceCoder

        return options
