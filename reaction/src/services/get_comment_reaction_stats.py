from db.redis_client import get_redis_client
from collections import Counter

def get_comment_reaction_stats(comment_id):
    """
    Récupère les statistiques des réactions associées à un commentaire.
    """
    client = get_redis_client()
    reactions = client.lrange(f"reactions:comments:{comment_id}", 0, -1)
    
    reaction_types = [eval(reaction.decode())['reaction'] for reaction in reactions]
    return dict(Counter(reaction_types))
