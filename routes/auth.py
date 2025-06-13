from flask import Blueprint, request, jsonify
from models import User
from extensions import db, bcrypt
from services import TokenService

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data or "email" not in data or "password" not in data:
        return jsonify({"error": "Missing fields"}), 400

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "User already exists"}), 409

    user = User(email=data["email"])
    user.password = data["password"]  # автоматически хэшируется через setter
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or "email" not in data or "password" not in data:
        return jsonify({"error": "Missing fields"}), 400

    user = User.query.filter_by(email=data["email"]).first()
    if user and bcrypt.check_password_hash(user._password, data["password"]):
        token = TokenService.create_token(user_id=user.id)
        return jsonify({"token": token}), 200

    return jsonify({"error": "Invalid credentials"}), 401
