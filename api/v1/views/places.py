from flask import jsonify
from . import app


@app.route('/api/v1/places', methods=['GET'])
def get_places():
    # Lógica para obtener y retornar la lista de lugares
    places = [{"name": "Place1"}, {"name": "Place2"}, {"name": "Place3"}]
    return jsonify({"places": places})
