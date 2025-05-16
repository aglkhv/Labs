from models import User
from extensions import db

class UserRepository:
    @staticmethod
    def find_by_email(email: str) -> User | None:
        return User.query.filter_by(email=email).first()

    @staticmethod
    def add(user: User):
        db.session.add(user)
        db.session.commit()
