from flask import Blueprint, jsonify, request
from services.reaction_comment_service import add_reaction_to_comment

create_comment_reaction_bp = Blueprint('create_comment_reaction_bp', __name__)

@create_comment_reaction_bp.route('/comments/<comment_id>/reactions', methods=['POST'])
def add_reaction(comment_id):
    """
    Route pour ajouter une réaction à un commentaire.
    """
    try:
        # Récupérer les données du corps de la requête
        data = request.get_json()
        user_id = data.get("user_id")
        reaction = data.get("reaction")

        # Vérification des données requises
        if not user_id or not reaction:
            return jsonify({"error": "Les champs 'user_id' et 'reaction' sont obligatoires."}), 400

        # Appeler le service pour ajouter la réaction
        response = add_reaction_to_comment(comment_id, user_id, reaction)

        if response["success"]:
            return jsonify({"message": "Réaction ajoutée avec succès.", "reaction_id": response["reaction_id"]}), 201
        else:
            return jsonify({"error": f"Commentaire avec l'ID {comment_id} introuvable."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
