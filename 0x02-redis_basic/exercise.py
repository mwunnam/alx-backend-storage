#!/urs/bin/env python3
import redis
from uuid import uuid4
from typing import Union, Optional
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

    def get(
        self,
        key: str,
        fn: Optional[Callable[[bytes], Union[str, bytes, int, float]]] = None
    ) -> Optional[Union[str, bytes, int, float]]:
        data = self._redis.get(key)
        if data is None:
            return None

        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        return self.get(key, lambda x: x.decode('Utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        return self.get(key, lambda x: int(x))
