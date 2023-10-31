from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg:///cupcakes"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
    app.config["SECRET_KEY"] = "khkld#$nvc%retw$#%76Hc0fw$%!3"

    from routes import app_routes
    app.register_blueprint(app_routes)
    
    return app
