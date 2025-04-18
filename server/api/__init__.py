# external imports
from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from logging.config import dictConfig
from flask_jwt_extended import JWTManager

# internal imports
from api.config import Config
from api.errors import register_error_handlers
from api.utils.model_handling import load_captioning_model

mongo = PyMongo()
jwt = JWTManager()

def create_app(config_object = Config):
    dictConfig(config_object.LOGGING_CONFIG)
    app = Flask(__name__)
    app.config.from_object(config_object)
    
    CORS(
        app,
        origins=[app.config.get('CLIENT_URL')],
        allow_headers=['Authorization', 'Content-Type'],
        supports_credentials=True
    )
    mongo.init_app(app)
    jwt.init_app(app)

    register_error_handlers(app)

    try:
        app.blip_processor, app.blip_model = load_captioning_model('Salesforce/blip-image-captioning-base')    
    except RuntimeError as re:
        app.logger.error(str(re))

    # importing blueprints inside factory function to avoid circular import
    from api.users import user_bp
    from api.projects import proj_bp
    from api.sessions import sess_bp

    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(proj_bp, url_prefix='/projects')
    app.register_blueprint(sess_bp, url_prefix='/sessions')

    return app
