from db.redis_client import get_redis_client
import uuid

def add_tweet_reaction(tweet_id, user_id, reaction):
    """
    Ajoute une réaction à un tweet pour un utilisateur donné.
    Met également à jour les statistiques des réactions.
    """
    client = get_redis_client()
    
    # Clé pour stocker les réactions de ce tweet
    reactions_key = f'tweet:{tweet_id}:reactions'
    stats_key = f'tweet:{tweet_id}:reactions_stat'

    # Générer un ID unique pour la réaction
    reaction_id = str(uuid.uuid4())

    # Récupérer les réactions actuelles
    reactions = client.get(reactions_key)
    if reactions is None:
        reactions = []
    else:
        reactions = eval(reactions)  # Convertir les données en objets Python

    # Ajouter la nouvelle réaction
    reactions.append({"reaction_id": reaction_id, "user_id": user_id, "reaction": reaction})
    client.set(reactions_key, str(reactions))  # Mettre à jour Redis

    # Mettre à jour les statistiques des réactions
    stats = client.get(stats_key)
    if stats is None:
        stats = {}
    else:
        stats = eval(stats)  # Convertir les données en objets Python

    # Incrémenter la statistique de la réaction correspondante
    stats[reaction] = stats.get(reaction, 0) + 1
    client.set(stats_key, str(stats))  # Mettre à jour Redis

    return {"reaction_id": reaction_id, "success": True}
