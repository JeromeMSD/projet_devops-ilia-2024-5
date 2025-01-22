from db.redis_client import get_redis_client

def has_user_reacted(user_id, item_id, item_type, reaction):
    """
    Vérifie si un utilisateur a déjà réagi avec une réaction spécifique à un tweet ou commentaire.
    """
    client = get_redis_client()
    key = f"reactions:{item_type}s:{item_id}"
    reactions = client.lrange(key, 0, -1)
    
    for r in reactions:
        reaction_data = eval(r.decode())
        if reaction_data['user_id'] == user_id and reaction_data['reaction'] == reaction:
            return True
    return False
