from flask import Blueprint
from .routes import index
from . import gallery

bp = Blueprint('main', __name__)

bp.add_url_rule('/', 'index', index, methods=['GET'])

bp.register_blueprint(gallery.bp)
