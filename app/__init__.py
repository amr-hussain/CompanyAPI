""" 
app/__init__.py
It is the application factory.
Creates and configures the Flask app.
Registers blueprints (your routes).
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

jwt = JWTManager()

# Global db instance to use in models
db = SQLAlchemy()
migrate = Migrate()
def create_app():
    app = Flask(__name__)

    # Initialize JWT Manager
    jwt.init_app(app)

    # Load configuration
    app.config.from_object('app.config.Config')

    # initializing the database with the application 
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Import Blueprints
    from app.routes.company_routes import company_bp, auth_bp
    app.register_blueprint(company_bp, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    return app
