from db.redis_client import get_redis_client

def get_tweet_reactions(tweet_id):
    client = get_redis_client()
    
    # fetch reactions for the given tweet_id from Redis
    reactions = client.get(f'tweet:{tweet_id}:reactions')
    
    if reactions is None:
        # Return an empty list if no reactions are found
        reactions = []
    else:
        # Convert string data to Python objects (assuming Redis stores it as a string)
        reactions = eval(reactions)
    
    return reactions
