import redis
import os

def get_redis_client():
    redis_host = os.getenv('REDIS_HOST','localhost')
    print("*********************************************************")
    print(redis_host)
    redis_port = int(os.getenv('REDIS_PORT',6379))
    return redis.Redis(host=redis_host, port=redis_port, db=0)