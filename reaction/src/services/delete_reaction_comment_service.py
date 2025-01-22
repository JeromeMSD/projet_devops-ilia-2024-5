import json
from db.redis_client import get_redis_client

def delete_reaction_comment(comment_id, reaction_id):
    """
    Supprime une réaction d'un commentaire pour un identifiant de réaction donné.
    Met également à jour les statistiques des réactions.
    """
    client = get_redis_client()
    
    # Clés pour les réactions et les statistiques
    reactions_key = f'comment:{comment_id}:reactions'
    stats_key = f'comment:{comment_id}:reactions_stat'

    # Récupérer les réactions actuelles
    reactions = client.get(reactions_key)
    if reactions is None:
        return {"success": False, "error": "No reactions found for this comment."}

    # Convertir les données en objets Python
    reactions = eval(reactions)

    # Trouver la réaction à supprimer
    reaction_to_remove = next((reaction for reaction in reactions if reaction['reaction_id'] == reaction_id), None)
    if not reaction_to_remove:
        return {"success": False, "error": "Reaction ID not found."}

    # Supprimer la réaction
    updated_reactions = [reaction for reaction in reactions if reaction['reaction_id'] != reaction_id]
    client.set(reactions_key, str(updated_reactions))  # Mettre à jour Redis

    # Mettre à jour les statistiques des réactions
    stats = client.get(stats_key)
    if stats is not None:
        stats = eval(stats)  # Convertir les données en objets Python
        reaction_type = reaction_to_remove['reaction']
        if reaction_type in stats:
            stats[reaction_type] = max(stats[reaction_type] - 1, 0)  # Empêcher un compteur négatif
            client.set(stats_key, str(stats))  # Mettre à jour Redis

    return {"success": True}
