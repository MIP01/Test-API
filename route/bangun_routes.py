from flask import Blueprint
from controller.bangun_controller import create_bangun_handler, get_bangun_handler, delete_bangun_handler

bangun_bp = Blueprint('bangun_bp', __name__)

bangun_bp.route('/bangun', methods=['POST'])(create_bangun_handler)
bangun_bp.route('/bangun', methods=['GET'])(get_bangun_handler)
bangun_bp.route('/bangun/<int:bangun_id>', methods=['DELETE'])(delete_bangun_handler)
