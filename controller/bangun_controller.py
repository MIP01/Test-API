from flask import request, jsonify
from module.bangun_module import create_bangun, get_banguns, delete_bangun

def create_bangun_handler():
    data = request.get_json()
    bangun, status_code = create_bangun(data)
    
    if isinstance(bangun, dict) and 'error' in bangun:
        return jsonify(bangun), status_code

    return jsonify(bangun), 201

def get_bangun_handler():
    banguns = get_banguns()
    return jsonify(banguns), 200
       
def delete_bangun_handler(bangun_id):
    result, status_code = delete_bangun(bangun_id)
    
    if isinstance(result, dict) and 'error' in result:
        return jsonify(result), status_code

    return jsonify(result), status_code