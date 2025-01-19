from db.redis_client import get_redis_client

def delete_comment_by_id(comment_id):
    """
    Supprime un commentaire spécifique en utilisant son ID dans Redis.
    """
    client = get_redis_client()

    # Récupérer tous les commentaires
    comments = client.lrange("comments", 0, -1)

    if comments:
        for comment in comments:
            comment_data = eval(comment.decode())  # Convertir le commentaire en dict
            if comment_data["id"] == comment_id:
                # Supprimer le commentaire correspondant
                client.lrem("comments", 0, comment)
                return True

    # Si le commentaire n'est pas trouvé
    return False
