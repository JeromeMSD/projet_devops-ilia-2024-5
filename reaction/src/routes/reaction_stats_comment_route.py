from flask import Blueprint, jsonify
from services.get_comment_reaction_stats import get_comment_reaction_stats

comment_reaction_stats_bp = Blueprint('comment_reaction_stats', __name__)

@comment_reaction_stats_bp.route('/comments/<comment_id>/reactions/stats', methods=['GET'])
def get_comment_reaction_stats_route(comment_id):
    stats = get_comment_reaction_stats(comment_id)
    return jsonify(stats), 200
