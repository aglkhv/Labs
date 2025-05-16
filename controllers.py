from flask import Blueprint, request, jsonify
from models import User
from repositories import UserRepository
from services import TokenService

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    if UserRepository.find_by_email(data["email"]):
        return jsonify({"error": "Email taken"}), 400

    user = User(email=data["email"])
    user.password = data["password"]
    UserRepository.add(user)
    return jsonify({"message": "User created"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = UserRepository.find_by_email(data["email"])
    if not user or not user.verify_password(data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    token = TokenService.create_token(user.id)
    return jsonify({"token": token}), 200
