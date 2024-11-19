from flask import Blueprint

sess_bp = Blueprint('sessions', __name__)

from . import routes