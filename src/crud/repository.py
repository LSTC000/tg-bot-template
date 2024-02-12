from src import models

from .abc import ABCCRUDRepository
from .user import UserCRUD


class CRUDRepository(ABCCRUDRepository):
    user: UserCRUD = UserCRUD(models.User)
