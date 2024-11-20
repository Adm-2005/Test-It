from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager

mongo = PyMongo()
jwt = JWTManager()

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    
    mongo.init_app(app)
    jwt.init_app(app)

    #importing blueprints inside factory function to avoid circular import
    from api.auth import auth_bp
    from api.model import model_bp
    from api.projects import proj_bp
    from api.sessions import sess_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(proj_bp, url_prefix="/projects")
    app.register_blueprint(sess_bp, url_prefix="/sessions")
    app.register_blueprint(model_bp, url_prefix="/model")

    return app
