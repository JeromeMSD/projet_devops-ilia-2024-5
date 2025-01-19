
from flask import Blueprint, jsonify
from services.get_reactions_from_comments_services import get_comments_reactions

comment_reaction_bp = Blueprint('comment_reactions', __name__)

@comment_reaction_bp.route('/comment/<int:comment_id>/reactions', methods=['GET'])
def get_reactions(comment_id):
    try:
        reactions = get_comments_reactions(comment_id)
        return jsonify(reactions), 200
    except KeyError:
        return jsonify({"error": f"No reactions found for tweet_id {comment_id}"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
