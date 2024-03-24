from flask import Blueprint
from .routes import index, create_picture, create_collection, update_picture, update_collection, delete_picture, \
    delete_collection

bp = Blueprint('panel', __name__, url_prefix='/panel', template_folder='panel')
bp.add_url_rule('/', 'index', index, methods=['GET'])
bp.add_url_rule('/picture/create', 'create_picture', create_picture, methods=['GET', 'POST'])
bp.add_url_rule('/collection/create', 'create_collection', create_collection, methods=['GET', 'POST'])
bp.add_url_rule('/picture/update', 'update_picture', update_picture, methods=['POST'])
bp.add_url_rule('/collection/update', 'update_collection', update_collection, methods=['POST'])
bp.add_url_rule('/picture/delete', 'delete_picture', delete_picture, methods=['POST'])
bp.add_url_rule('/collection/delete', 'delete_collection', delete_collection, methods=['POST'])
