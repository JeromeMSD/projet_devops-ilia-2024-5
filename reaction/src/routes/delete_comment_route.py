from flask import Blueprint, jsonify
from services.delete_comment_service import delete_comment_by_id

delete_comment_bp = Blueprint('comments', __name__)

@delete_comment_bp.route('/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    """
    Route pour supprimer un commentaire par son ID.
    """
    try:
        # Appeler le service pour supprimer le commentaire
        success = delete_comment_by_id(comment_id)

        if success:
            return jsonify({"message": "Commentaire supprimé avec succès."}), 200
        else:
            return jsonify({"error": f"Commentaire avec l'ID {comment_id} introuvable."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
