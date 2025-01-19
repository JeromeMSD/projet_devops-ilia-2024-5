from db.redis_client import get_redis_client
import uuid
from datetime import datetime

def get_comments(tweet_id):
    """
    Récupère tous les commentaires associés à un tweet spécifique.
    """
    client = get_redis_client()
    comments_data = client.lrange(f"comments:{tweet_id}", 0, -1)
    
    comments = []
    for comment in comments_data:
        comment_dict = eval(comment.decode())  # Convertir la chaîne en dictionnaire
        comments.append(comment_dict)
    
    return comments