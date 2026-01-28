from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET"])
def dashboard():
    return render_template("dashboard.html")

@main_bp.route("/dashboard", methods=["GET"])
def dashboard_page():
    return render_template("dashboard.html")

@main_bp.route("/transaction", methods=["GET"])
def transaction_page():
    return render_template("transaction.html")
