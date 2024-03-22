from flask import Blueprint
from .routes import collections

bp = Blueprint('gallery', __name__, url_prefix='/gallery')

bp.add_url_rule('/', 'index', collections, methods=['GET'])
