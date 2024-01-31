from flask import jsonify
from . import app


@app.route('/api/v1/amenities', methods=['GET'])
def get_amenities():
    # Lógica para obtener y retornar la lista de comodidades
    amenities = ["Amenity1", "Amenity2", "Amenity3"]
    return jsonify({"amenities": amenities})
