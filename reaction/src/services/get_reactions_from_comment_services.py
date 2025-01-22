from db.redis_client import get_redis_client

def get_comment_reactions(comment_id):
    client = get_redis_client()
    
    # fetch reactions for the given comment_id from Redis
    # key_type = client.type(f'comment:{comment_id}:reactions')

    # return f'Type of key: {key_type}'

    reactions = client.get(f'comment:{comment_id}:reactions')
    
    if reactions is None:
        # Return an empty list if no reactions are found
        reactions = []
    else:
        # Convert string data to Python objects (assuming Redis stores it as a string)
        reactions = eval(reactions)

    return reactions
