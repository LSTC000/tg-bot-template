from datetime import datetime

import pytz

from src.config.settings import settings


class DateTimeManager:
    _default_tz: str = settings.postgres.TZ

    @staticmethod
    def get_datetime() -> datetime:
        return datetime.now().replace(microsecond=0)

    @classmethod
    def get_datetime_w_timezone(cls, timezone: str | None = None) -> datetime:
        if not timezone:
            timezone = cls._default_tz
        return datetime.now().replace(microsecond=0).astimezone(pytz.timezone(timezone))
