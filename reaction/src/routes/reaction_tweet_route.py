from flask import Blueprint, jsonify, request
from services.reaction_tweet_service import add_tweet_reaction

reaction_bp = Blueprint('reactions', __name__)

@reaction_bp.route('/tweets/<int:tweet_id>/reactions', methods=['POST'])
def add_reaction(tweet_id):
    try:
        # Récupérer les données de la requête
        data = request.get_json()
        user_id = data.get('userId')
        reaction = data.get('reaction')

        if not user_id or not reaction:
            return jsonify({"error": "Les champs 'userId' et 'reaction' sont obligatoires."}), 400

        # Ajouter la réaction via le service
        success = add_tweet_reaction(tweet_id, user_id, reaction)

        if success:
            return jsonify({"message": "Réaction ajoutée avec succès."}), 201
        else:
            return jsonify({"error": "Impossible d'ajouter la réaction."}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
