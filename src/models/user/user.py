from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, mapped_column

from src.config.db import Base
from src.schemas import DBSchemas

from ..mixins import DateTimeMixin


USER_SCHEMA = DBSchemas.USER.value


class User(Base, DateTimeMixin):
    """
    Table With User Data
    """

    __tablename__ = "user"
    __table_args__ = {"schema": USER_SCHEMA, "comment": "Table with all users"}

    sid: Mapped[UUID] = mapped_column(
        unique=True, primary_key=True, index=True, default=uuid4
    )

    tg_id: Mapped[str] = mapped_column(comment="Telegram ID of user")
    name: Mapped[str] = mapped_column(comment="Telegram name of user")
    email: Mapped[str | None] = mapped_column(unique=True, comment="Email of user")
    phone: Mapped[str | None] = mapped_column(
        unique=True, comment="Telegram phone number of user"
    )
    hashed_password: Mapped[str | None] = mapped_column(
        comment="Hashed password of user"
    )

    is_active: Mapped[bool] = mapped_column(
        default=True, comment="Active status of user"
    )

    def __init__(
        self,
        tg_id: str,
        name: str,
        email: str | None = None,
        phone: str | None = None,
        hashed_password: str | None = None,
        is_active: bool = True,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
    ):
        self.sid: UUID = uuid4()

        self.tg_id: str = tg_id
        self.name: str = name
        self.email: str | None = email
        self.phone: str | None = phone
        self.hashed_password: str | None = hashed_password

        self.is_active: bool = is_active

        self.created_at: datetime | None = created_at
        self.updated_at: datetime | None = updated_at

    def __repr__(self):
        return (
            f"<{self.__class__.__name__}("
            f"sid={self.sid}, "
            f"name={self.name}, "
            f"email={self.email}, "
            f"phone={self.phone}, "
            f"hashed_password={self.hashed_password}, "
            f"is_active={self.is_active}, "
            f"created_at={self.created_at}, "
            f"updated_at={self.updated_at})>"
        )
