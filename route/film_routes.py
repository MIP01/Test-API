from flask import Blueprint
from controller.film_controller import create_film_handler, get_films_handler, get_film_by_genre_handler, delete_film_handler

film_bp = Blueprint('film_bp', __name__)

film_bp.route('/film', methods=['POST'])(create_film_handler)
film_bp.route('/film', methods=['GET'])(get_films_handler)
film_bp.route('/film/<string:genre>', methods=['GET'])(get_film_by_genre_handler)
film_bp.route('/film/<int:id>', methods=['DELETE'])(delete_film_handler)
