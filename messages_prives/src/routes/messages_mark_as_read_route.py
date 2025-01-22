from flask import Blueprint, jsonify
from services.messages_mark_as_read_service import mark_as_read

message_mark_as_read_bp = Blueprint('message_mark_as_read', __name__)

@message_mark_as_read_bp.route('/messages/<int:message_id>', methods=['PUT'])
def update_message_status(message_id):
    """
    Route pour marquer un message comme lu
    """
    try:
        if mark_as_read(message_id):
            return jsonify({"messageId": message_id, "status": "Message marqué comme lu avec succès"}), 200
        return jsonify({"error": f"Message introuvable {message_id}"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
