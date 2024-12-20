from flask import Blueprint
from controller.user_controller import create_user_handler, get_users_handler, delete_user_handler

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/user', methods=['POST'])(create_user_handler)
user_bp.route('/user', methods=['GET'])(get_users_handler)
user_bp.route('/user/<int:user_id>', methods=['DELETE'])(delete_user_handler)
