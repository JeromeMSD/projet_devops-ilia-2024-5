from flask import Blueprint, jsonify, request
from services.messages_send_service import send_message

messages_send_bp = Blueprint('messages_send', __name__)

@messages_send_bp.route('/messages', methods=['POST'])
def create_message():
    """
    Route pour envoyer un message privé.
    """
    try:
        data = request.get_json()
        sender = data.get("sender")
        receiver = data.get("receiver")
        content = data.get("content")

        if not sender or not receiver or not content:
            return jsonify({"error": "Les champs 'sender', 'receiver', et 'content' sont obligatoires."}), 400

        message_id = send_message(sender, receiver, content)
        return jsonify({"messageId": message_id, "status": "Message envoyé avec succès"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
