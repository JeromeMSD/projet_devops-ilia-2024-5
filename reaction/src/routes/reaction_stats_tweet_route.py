from flask import Blueprint, jsonify
from services.get_tweet_reaction_stats import get_tweet_reaction_stats

reaction_stats_bp = Blueprint('reaction_stats', __name__)

@reaction_stats_bp.route('/tweets/<tweet_id>/reactions/stats', methods=['GET'])
def get_tweet_reaction_stats_route(tweet_id):
    stats = get_tweet_reaction_stats(tweet_id)
    return jsonify(stats), 200
