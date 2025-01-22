from database.database import messages, message_counter  
 
def send_message(sender, receiver, content):
    """
    Envoie un nouveau message.
    """
    global messages, message_counter
    message_id = message_counter
    messages[message_id] = {
        "sender": sender,
        "receiver": receiver,
        "content": content,
        "isRead": False
    }
    message_counter += 1
    print(messages)
    return message_id