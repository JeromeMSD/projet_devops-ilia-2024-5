from flask import Blueprint, jsonify, request
from services.check_user_reaction_service import has_user_reacted

reaction_check_bp = Blueprint('reaction_check', __name__)

@reaction_check_bp.route('/reactions/check', methods=['GET'])
def check_user_reaction():
    user_id = request.args.get('user_id')
    item_id = request.args.get('item_id')
    item_type = request.args.get('item_type')  # "tweet" ou "comment"
    reaction = request.args.get('reaction')
    
    has_reacted = has_user_reacted(user_id, item_id, item_type, reaction)
    return jsonify({"has_reacted": has_reacted}), 200
