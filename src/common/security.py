from passlib.context import CryptContext


class SecurityManager:
    _pwd_context: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return cls._pwd_context.verify(plain_password, hashed_password)

    @classmethod
    def get_password_hash(cls, password: str | None) -> str | None:
        if password is None:
            return None
        return cls._pwd_context.hash(password)
