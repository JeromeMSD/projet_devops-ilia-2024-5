from database.database import messages

def get_conversation_messages(user1, user2):
    """
    Récupère les messages entre deux users
    """
    return [
        {"id": msg_id, **msg}
        for msg_id, msg in messages.items()
        if (msg["sender"] == user1 and msg["receiver"] == user2) or
           (msg["sender"] == user2 and msg["receiver"] == user1)
    ]