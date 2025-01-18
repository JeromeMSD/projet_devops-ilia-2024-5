from flask import Blueprint, jsonify
from services.supp_comment_service import delete_comment_by_id

# Blueprint pour les routes liées aux commentaires
supp_comment_bp = Blueprint('supp_comments', __name__)

@supp_comment_bp.route('/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    """
    Route pour supprimer un commentaire par son ID.
    """
    try:
        success = delete_comment_by_id(comment_id)
        if success:
            return jsonify({"message": "Commentaire supprimé avec succès."}), 200
        else:
            return jsonify({"error": f"Commentaire avec l'ID {comment_id} non trouvé."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
