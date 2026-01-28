from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')

    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    from app.api.routes import api_bp
    from app.auth.routes import auth_bp
    from app.main.routes import main_bp

    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(main_bp)

    return app
