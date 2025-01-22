from flask import jsonify, request
from src.routes.blueprint import bp

@bp.route('/tweet', methods=['POST'])
def create_tweet():
    content = request.json.get('content')
    if not content:
        return jsonify({"message": "Invalid input"}), 400
    # Logic to create a tweet (e.g., save to database)
    tweet = {
        "id": 1,  # This should be dynamically generated
        "message": content,
        "author": "BiduleLaCartouse",  # This should be dynamically set
        "reaction": {
            "like": 0,
            "comment": 0,
            "retweet": 0
        }
    }
    return jsonify(tweet), 201