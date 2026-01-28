from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Transaction, User
from app import db

api_bp = Blueprint("api", __name__)

@api_bp.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "API alive"}), 200

@api_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    user = get_jwt_identity()
    return jsonify({"message": f"Hello {user}, JWT works"}), 200

@api_bp.route("/stats", methods=["GET"])
@jwt_required()
def stats():
    username = get_jwt_identity()
    user = User.query.filter_by(username=username).first()
    
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    transactions = Transaction.query.filter_by(user_id=user.id).all()
    
    return jsonify({
        "total": len(transactions),
        "amounts": [t.amount for t in transactions]
    }), 200

@api_bp.route("/transaction", methods=["POST"])
@jwt_required()
def create_transaction():
    username = get_jwt_identity()
    user = User.query.filter_by(username=username).first()
    
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    try:
        data = request.get_json()
        
        if not data or not data.get("amount"):
            return jsonify({"error": "Amount is required"}), 400
        
        amount = float(data["amount"])
        
        if amount <= 0:
            return jsonify({"error": "Amount must be greater than 0"}), 400
        
        transaction = Transaction(user_id=user.id, amount=amount)
        db.session.add(transaction)
        db.session.commit()
        
        return jsonify({
            "message": "Transaction created",
            "id": transaction.id,
            "amount": transaction.amount,
            "timestamp": transaction.timestamp.isoformat()
        }), 201
    except ValueError:
        return jsonify({"error": "Invalid amount format"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
