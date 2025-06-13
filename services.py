import jwt
from datetime import datetime, timedelta, UTC
from config import Config

class PasswordHasher:
    @staticmethod
    def hash(raw: str) -> str:
        import bcrypt
        return bcrypt.hashpw(raw.encode(), bcrypt.gensalt()).decode()

    @staticmethod
    def verify(raw: str, hashed: str) -> bool:
        import bcrypt
        return bcrypt.checkpw(raw.encode(), hashed.encode())

class TokenService:
    @staticmethod
    def create_token(user_id: int) -> str:
        payload = {
            "sub": str(user_id),
            "exp": datetime.now(UTC) + timedelta(hours=2)
        }
        return jwt.encode(payload, Config.SECRET_KEY, algorithm=Config.JWT_ALGORITHM)