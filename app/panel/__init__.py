from flask import Blueprint
from .routes import index, create_picture, create_collection, update_picture, update_collection, delete_picture, \
    delete_collection

bp = Blueprint('panel', __name__, url_prefix='/panel', template_folder='panel')
bp.add_url_rule('/', 'index', index, methods=['GET'])
bp.add_url_rule('/upload', 'upload', create_picture, methods=['GET', 'POST'])
bp.add_url_rule('/collection', 'new_collection', create_collection, methods=['GET', 'POST'])
