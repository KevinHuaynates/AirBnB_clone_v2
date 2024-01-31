from flask import jsonify
from . import app


@app.route('/api/v1/cities', methods=['GET'])
def get_cities():
    # Aquí iría la lógica para obtener y retornar la lista de ciudades
    cities = ["City1", "City2", "City3"]
    return jsonify({"cities": cities})
