from services import TokenService
import jwt
from config import Config

def test_token_creation_and_decoding():
    token = TokenService.create_token(user_id=42)
    decoded = jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.JWT_ALGORITHM])
    assert decoded["sub"] == "42"