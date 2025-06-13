
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from functools import wraps
import jwt

from config import Config
from extensions import db, bcrypt
from models import User
from services import TokenService
from routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)

    def token_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            auth_header = request.headers.get("Authorization")
            if not auth_header or not auth_header.startswith("Bearer "):
                return jsonify({"error": "Token missing"}), 401
            token = auth_header.split()[1]
            try:
                data = jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.JWT_ALGORITHM])
            except jwt.exceptions.InvalidTokenError:
                return jsonify({"error": "Invalid token"}), 401
            return f(user_id=data["sub"], *args, **kwargs)
        return decorated

    @app.route("/profile", methods=["GET"])
    @token_required
    def profile(user_id):
        user = db.session.get(User, int(user_id))
        if not user:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"email": user.email})

    app.register_blueprint(auth_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
