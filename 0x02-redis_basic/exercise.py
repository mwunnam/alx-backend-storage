#!/urs/bin/env python3
import redis
import uuid
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
        key = str(uuid.uuid4())
        sefl._redis.set(key, data)
        return key
