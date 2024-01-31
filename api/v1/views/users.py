from flask import jsonify
from . import app


@app.route('/api/v1/users', methods=['GET'])
def get_users():
    # Lógica para obtener y retornar la lista de usuarios
    users = [{"name": "User1"}, {"name": "User2"}, {"name": "User3"}]
    return jsonify({"users": users})
