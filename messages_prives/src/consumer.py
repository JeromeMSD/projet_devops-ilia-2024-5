class Consumer:
    def __init__(self, redis_client):
        self.redis_client = redis_client

    def process_message(self, message):
        if not message:
            return None
        
        key = message.get("key")
        value = message.get("value")
        if key and value:
            self.redis_client.set(key, value)