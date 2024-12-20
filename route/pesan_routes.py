from flask import Blueprint
from controller.pesan_controller import create_pesan_handler, get_pesans_handler, delete_pesan_handler

pesan_bp = Blueprint('pesan_bp', __name__)

pesan_bp.route('/feedback', methods=['POST'])(create_pesan_handler)
pesan_bp.route('/feedback', methods=['GET'])(get_pesans_handler)
pesan_bp.route('/feedback/<int:pesan_id>', methods=['DELETE'])(delete_pesan_handler)
