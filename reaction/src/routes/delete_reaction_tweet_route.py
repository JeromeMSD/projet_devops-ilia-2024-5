from flask import Blueprint, jsonify, request
from services.delete_tweet_reaction_service import delete_reaction

tweet_reaction_bp = Blueprint("tweet_reaction_bp", __name__)

@tweet_reaction_bp.route('/tweets/<tweet_id>/reactions/<reaction_id>', methods=['DELETE'])
def delete_tweet_reaction(tweet_id, reaction_id):
    result = delete_reaction(tweet_id, reaction_id)
    if result:
        return jsonify({"message": "Réaction supprimée avec succès."}), 200
    else:
        return jsonify({"error": "Réaction non trouvée ou déjà supprimée."}), 404
