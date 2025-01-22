from db.redis_client import get_redis_client

def add_reaction_to_comment(comment_id, user_id, reaction):
    """
    Ajoute une réaction à un commentaire spécifique dans Redis.
    """
    client = get_redis_client()
    
    # Clé pour stocker les réactions de ce comment
    key = f'comment:{comment_id}:reactions'

    # Récupérer les réactions actuelles
    reactions = client.get(key)
    if reactions is None:
        # Aucune réaction enregistrée, initialiser une liste
        reactions = []
    else:
        # Convertir les données en objets Python
        reactions = eval(reactions)

    # Ajouter la nouvelle réaction
    reactions.append({"user_id": user_id, "reaction": reaction})

    # Mettre à jour Redis
    client.set(key, str(reactions))

    return True
