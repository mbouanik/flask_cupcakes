from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os


db = SQLAlchemy()
load_dotenv()
def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("URI")
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
    app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')

    from routes import app_routes
    app.register_blueprint(app_routes)
    
    return app
