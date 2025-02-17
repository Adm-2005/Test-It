from flask import Blueprint

user_bp = Blueprint('users', __name__)

from . import auth_routes, profile_routes