from db.redis_client import get_redis_client

def add_reaction_to_comment(comment_id, user_id, reaction):
    """
    Ajoute une réaction à un commentaire spécifique dans Redis.
    """
    client = get_redis_client()

    # Clé Redis pour le commentaire
    key = f"comment:{comment_id}:reactions"

    # Récupérer les réactions existantes
    reactions = client.lrange(key, 0, -1)
    if reactions is None:
        reactions = []

    # Ajouter la nouvelle réaction
    new_reaction = {
        "user_id": user_id,
        "reaction": reaction
    }
    client.rpush(key, str(new_reaction))

    return True
