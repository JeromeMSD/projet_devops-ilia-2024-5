from flask import Blueprint, jsonify
from services.get_reactions_from_comment_services import get_comment_reactions

comment_reaction_bp = Blueprint('comment_reaction_bp', __name__)

@comment_reaction_bp.route('/comments/<comment_id>/reactions', methods=['GET'])
def get_reactions(comment_id):
    try:
        reactions = get_comment_reactions(comment_id)
        return jsonify(reactions), 200
    except KeyError:
        return jsonify({"error": f"No reactions found for comment_id {comment_id}"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
