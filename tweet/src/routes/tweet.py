from flask import jsonify, request
from src.routes.blueprint import bp

@bp.route('/tweet', methods=['POST'])
def tweet():
    content = request.json.get('content')
    # Logic to create a tweet
    return jsonify({"message": "Tweet created successfully"}), 200