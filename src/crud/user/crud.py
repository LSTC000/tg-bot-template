from src.models import User
from src.schemas import UserCreate, UserUpdate

from ..core import CoreCRUD


class UserCRUD(CoreCRUD[User, UserCreate, UserUpdate]):
    pass
