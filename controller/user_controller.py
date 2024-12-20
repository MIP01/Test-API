from flask import request, jsonify
from module.user_module import create_user, get_users, delete_user

def create_user_handler():
    data = request.get_json()
    user, status_code = create_user(data)
    
    if isinstance(user, dict) and 'error' in user:
        return jsonify(user), status_code

    return jsonify(user), 201

def get_users_handler():
    users = get_users()
    return jsonify(users), 200
       
def delete_user_handler(user_id):
    result, status_code = delete_user(user_id)
    
    if isinstance(result, dict) and 'error' in result:
        return jsonify(result), status_code

    return jsonify(result), status_code