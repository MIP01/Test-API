from flask import request, jsonify
from module.pesan_module import create_pesan, get_pesans, delete_pesan

def create_pesan_handler():
    data = request.get_json()
    pesan, status_code = create_pesan(data)
    
    if isinstance(pesan, dict) and 'error' in pesan:
        return jsonify(pesan), status_code

    return jsonify(pesan), 201

def get_pesans_handler():
    pesans = get_pesans()
    return jsonify(pesans), 200
       
def delete_pesan_handler(pesan_id):
    result, status_code = delete_pesan(pesan_id)
    
    if isinstance(result, dict) and 'error' in result:
        return jsonify(result), status_code

    return jsonify(result), status_code