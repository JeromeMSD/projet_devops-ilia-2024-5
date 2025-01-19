from db.redis_client import get_redis_client

def delete_reaction(tweet_id, reaction_id):
    client = get_redis_client()
    reaction_key = f"tweet:{tweet_id}:reactions"

    # Supprime la réaction spécifiée
    if client.hdel(reaction_key, reaction_id):
        return True  # Réaction supprimée avec succès
    return False  # Réaction non trouvée
