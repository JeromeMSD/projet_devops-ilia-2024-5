from db.redis_client import get_redis_client

def get_comments_reactions(comment_id):
    client = get_redis_client()
    
    # fetch reactions for the given tweet_id from Redis
    comment_reactions = client.get(f'comment:{comment_id}:reactions')
    
    if comment_reactions is None:
        # Return an empty list if no reactions are found
        comment_reactions = []
    else:
        # Convert string data to Python objects (assuming Redis stores it as a string)
        comment_reactions = eval(comment_reactions)
    
    return comment_reactions
