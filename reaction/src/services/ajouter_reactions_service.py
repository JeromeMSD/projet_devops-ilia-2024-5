from db.redis_client import get_redis_client

def add_tweet_reaction(tweet_id, user_id, reaction):
    """
    Ajoute une réaction à un tweet pour un utilisateur donné.
    """
    client = get_redis_client()
    
    # Clé pour stocker les réactions de ce tweet
    key = f'tweet:{tweet_id}:reactions'

    # Récupérer les réactions actuelles
    reactions = client.get(key)
    if reactions is None:
        # Aucune réaction enregistrée, initialiser une liste
        reactions = []
    else:
        # Convertir les données en objets Python
        reactions = eval(reactions)

    # Ajouter la nouvelle réaction
    reactions.append({"userId": user_id, "reaction": reaction})

    # Mettre à jour Redis
    client.set(key, str(reactions))

    return True
