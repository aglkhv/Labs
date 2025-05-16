from extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    _password = db.Column("password", db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def password(self):
        raise AttributeError("Password is write-only")

    @password.setter
    def password(self, raw: str):
        from services import PasswordHasher
        self._password = PasswordHasher.hash(raw)

    def verify_password(self, raw: str) -> bool:
        from services import PasswordHasher
        return PasswordHasher.verify(raw, self._password)
