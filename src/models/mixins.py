from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.common.datetime import DateTimeManager


class CreatedAtMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=DateTimeManager.get_datetime,
        comment="DateTime of create record",
    )


class UpdatedAtMixin:
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=DateTimeManager.get_datetime,
        onupdate=DateTimeManager.get_datetime,
        comment="DateTime of update record",
    )


class DateTimeMixin(CreatedAtMixin, UpdatedAtMixin):
    pass
