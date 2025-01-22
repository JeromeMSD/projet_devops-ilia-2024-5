from flask import Blueprint, jsonify
from services.get_reactions_from_tweet_services import get_tweet_reactions

tweet_reactions_bp = Blueprint('tweet_reactions_bp', __name__)

@tweet_reactions_bp.route('/tweets/<tweet_id>/reactions', methods=['GET'])
def get_reactions(tweet_id):
    try:
        reactions = get_tweet_reactions(tweet_id)
        return jsonify(reactions), 200
    except KeyError:
        return jsonify({"error": f"No reactions found for tweet_id {tweet_id}"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
