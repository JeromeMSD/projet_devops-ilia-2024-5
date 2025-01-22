from database.database import messages

def mark_as_read(message_id):
    """
    Marque un message comme lu
    """
    if message_id in messages and isinstance(messages[message_id], dict):
        messages[message_id]["isRead"] = True
        return True
    return False