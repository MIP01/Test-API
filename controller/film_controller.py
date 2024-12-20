from flask import request, jsonify
from module.film_module import create_film, get_films, get_film_by_genre, delete_film

def create_film_handler():
    data = request.get_json()
    film, status_code = create_film(data)
    
    if isinstance(film, dict) and 'error' in film:
        return jsonify(film), status_code

    return jsonify(film), 201

def get_films_handler():
    films = get_films()
    return jsonify(films), 200

def get_film_by_genre_handler(genre):
    film = get_film_by_genre(genre)

    # Tangani error jika ada
    if isinstance(film, dict) and 'error' in film:
        return jsonify(film), 400

    return jsonify(film), 200
       
def delete_film_handler(id):
    result, status_code = delete_film(id)
    
    if isinstance(result, dict) and 'error' in result:
        return jsonify(result), status_code

    return jsonify(result), status_code