import os
from dotenv import load_dotenv

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
load_dotenv(os.path.join(base_dir, '.env'))

class Config:
    TESTING = os.environ.get('TESTING', 'False').lower() in ['ok', 'true', 'yes']
    IMAGE_DIR = os.environ.get('IMAGE_DIR')
    CLIENT_URL = os.environ.get('CLIENT_URL')
    GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
    HF_TOKEN = os.environ.get('HF_TOKEN')
    MONGO_URI = os.environ.get('MONGO_URI')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'aslkdfjawoeijqo4eij')
    JWT_SECRET = os.environ.get('JWT_SECRET', 'zdskaoisefoewqweorwejakldsfawoeiiq132416459844i3dzk')
    JWT_ACCESS_TOKEN_EXPIRES = int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES', 18000)) # 5 hours = 5 * 60 * 60
    JWT_REFRESH_TOKEN_EXPIRES = int(os.environ.get('JWT_REFRESH_TOKEN_EXPIRES', 86400)) # 24 hours = 24 * 60 * 60
    LOGGING_CONFIG = {
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    }