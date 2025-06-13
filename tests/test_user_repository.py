from models import User
from repositories import UserRepository

def test_user_repository_add_and_find(app):
    user = User(email="test@example.com")
    user.password = "secure123"
    UserRepository.add(user)

    fetched = UserRepository.find_by_email("test@example.com")
    assert fetched is not None
    assert fetched.email == "test@example.com"