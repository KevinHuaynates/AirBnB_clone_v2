from flask import jsonify
from . import app


@app.route('/api/v1/states', methods=['GET'])
def get_states():
    # Lógica para obtener y retornar la lista de estados
    states = ["State1", "State2", "State3"]
    return jsonify({"states": states})
