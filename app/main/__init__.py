from flask import Blueprint
from .routes import index, pictures

bp = Blueprint('main', __name__)

bp.add_url_rule('/', 'index', index, methods=['GET'])
bp.add_url_rule('/pictures', 'pictures', pictures, methods=['GET'])
