from flask import Flask
from auth import auth_bp
from model import model_bp
from projects import proj_bp
from sessions import sess_bp

def create_app(config_module):
    app = Flask(__name__)
    
    

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(proj_bp, url_prefix="/projects")
    app.register_blueprint(sess_bp, url_prefix="/sessions")
    app.register_blueprint(model_bp, url_prefix="/model")

    return app
