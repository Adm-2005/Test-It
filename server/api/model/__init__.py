from flask import Blueprint

model_bp = Blueprint('model', __name__)

from . import routes