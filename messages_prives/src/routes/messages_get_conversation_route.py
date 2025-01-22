from flask import Blueprint, jsonify
from services.messages_get_conversation_service import get_conversation_messages

message_get_conversation_bp = Blueprint('message_get_conversation', __name__)

@message_get_conversation_bp.route('/messages/<user1>/<user2>', methods=['GET'])
def retrieve_messages(user1, user2):
    """
    Route pour récupérer les messages entre deux utilisateurs.
    """
    try:
        messages = get_conversation_messages(user1, user2)
        if not messages:
            return jsonify({"error": "Aucun message trouvé"}), 404
        return jsonify(messages), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
