from flask import jsonify
from . import app


@app.route('/api/v1/', methods=['GET'])
def get_index():
    return jsonify({"message": "Welcome to your API!"})
