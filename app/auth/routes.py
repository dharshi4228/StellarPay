from flask import Blueprint, request, jsonify, render_template
from app import db
from app.models import User
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    # POST method
    try:
        data = request.get_json()
        
        if not data or not data.get("username") or not data.get("password"):
            return jsonify({"error": "Username and password are required"}), 400
        
        if User.query.filter_by(username=data["username"]).first():
            return jsonify({"error": "User already exists"}), 409

        user = User(
            username=data["username"],
            password=generate_password_hash(data["password"]),
            role="user"
        )

        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "User registered"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    # POST method
    try:
        data = request.get_json()
        
        if not data or not data.get("username") or not data.get("password"):
            return jsonify({"error": "Username and password are required"}), 400
        
        user = User.query.filter_by(username=data["username"]).first()

        if not user or not check_password_hash(user.password, data["password"]):
            return jsonify({"error": "Invalid credentials"}), 401

        token = create_access_token(identity=user.username, additional_claims={"role": user.role})
        return jsonify({"access_token": token}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
