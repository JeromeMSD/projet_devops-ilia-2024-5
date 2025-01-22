from db.redis_client import get_redis_client
from collections import Counter

def get_tweet_reaction_stats(tweet_id):
    """
    Récupère les statistiques des réactions associées à un tweet.
    """
    client = get_redis_client()
    reactions = client.lrange(f"reactions:tweets:{tweet_id}", 0, -1)
    
    reaction_types = [eval(reaction.decode())['reaction'] for reaction in reactions]
    return dict(Counter(reaction_types))
