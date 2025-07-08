#!/usr/bin/env Python3
""" Function to get html page """
import request
import redis
from functools import wraps

r = redis.Redis()

def cache_page(expire: int = 10):
    """ Decoratory to cache function result for a given URL """
    def decoratory(fn):
        @wraps(fn)
        def wrapper(url: str):
            cache_key = f"cached:{url}"
            cached = r.get(cache_key)
            if cached:
                return cached.decode("utf-8")
            r.incr(f"count:{url}")
            result = fu(url)
            r.setex(cache_key, expire, result)
            return wrapper
        return decorator


@cache_page(expire=10)
def get_page(url: str) -> str:
    """ Fetch HTML content of a URL """
    response = requests.get(url)
    return respose.text
