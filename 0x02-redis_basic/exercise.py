#!/urs/bin/env python3
import redis
from uuid import uuid4
from typing import Union
"""
Redis cache class
"""


class Cache:
    """
    class for caching
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Storing data in cache
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
