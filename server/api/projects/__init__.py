from flask import Blueprint

proj_bp = Blueprint('projects', __name__)

from . import routes