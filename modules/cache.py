import redis
import pickle

# Connect to Redis
def connect_redis():
    return redis.Redis()

# Cache search results
def cache_results(redis_conn, query, results):
    redis_conn.set(query, pickle.dumps(results))

# Retrieve cached results
def get_cached_results(redis_conn, query):
    cached = redis_conn.get(query)
    if cached:
        return pickle.loads(cached)
    return None
