from uuid import UUID

from pydantic import EmailStr, Field

from ..core import CoreModel, DateTimeMixin


# --================ Base ================--
class UserBase(CoreModel):
    tg_id: str = Field(..., description="Telegram ID of user")
    name: str = Field(..., description="Telegram name of user")
    email: EmailStr | None = Field(None, description="Email of user")
    phone: str | None = Field(None, description="Telegram phone number of user")


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserUpdateMe(UserBase):
    pass


# --================ DB Base ================--
class UserInDBBase(UserBase, DateTimeMixin):
    sid: UUID = Field(..., description="SID of user")
    is_active: bool = Field(True, description="Active status of user")


class UserInDB(UserInDBBase):
    hashed_password: str = Field(..., description="Hashed password of user")


class User(UserInDBBase):
    pass
