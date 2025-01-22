from flask import Blueprint

from routes.messages_get_conversation_route import message_get_conversation_bp
from routes.messages_send_route import messages_send_bp
from routes.messages_mark_as_read_route import message_mark_as_read_bp

messages_bp = [
    message_get_conversation_bp,
    messages_send_bp,
    message_mark_as_read_bp
]
