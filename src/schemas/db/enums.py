from enum import Enum, unique


@unique
class DBSchemas(str, Enum):
    USER: str = "users"
