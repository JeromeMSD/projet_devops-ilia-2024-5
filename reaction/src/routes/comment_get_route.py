from flask import Blueprint, jsonify
from services.comment_service_get import get_comments

comment_get_bp = Blueprint('comment_get', __name__)

# Route pour récupérer les commentaires d'un tweet
@comment_get_bp.route('/tweets/<tweet_id>/comments', methods=['GET'])
def get_comment(tweet_id):
    comments = get_comments(tweet_id)
    return jsonify(comments), 200
