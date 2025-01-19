from flask import Blueprint, jsonify
from services.delete_reaction_on_tweet_service import delete_reaction_tweet

delete_reactions_tweet_bp = Blueprint('reactions', __name__)

@delete_reactions_tweet_bp.route('/comments/<comment_id>/reactions/<reaction_id>', methods=['DELETE'])
def delete_reaction_on_tweet(tweet_id, reaction_id):
    try:
        success = delete_reaction_on_tweet(tweet_id, reaction_id)
        if success:
            return jsonify({"message": "Reaction deleted successfully on tweet"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
