#!/usr/bin/env python3
import redis
from typing import Union, Callable, Optional
import uuid
from functools import wraps


def replay(method: Callable):
    """Display the history of calls of a particular function"""
    redis_client = method.__self__._redis
    key = method.__qualname__

    inputs_key = f"{key}:inputs"
    outputs_key = f"{key}:outputs"

    inputs = redis_client.lrange(inputs_key, 0, -1)
    outputs = redis_client.lrange(outputs_key, 0, -1)

    call_count = redis_client.get(key)
    if call_count is not None:
        call_count = int(call_count)
    else:
        call_count = 0

    print(f"{key} was called {call_count} times:")

    for input_args, output in zip(inputs, outputs):
        input_str = input_args.decode("utf-8")
        output_str = output.decode("utf-8")
        print(f"{key}(*{input_str}) -> {output_str}")


def count_calls(method: Callable) -> Callable:
    """ Decorator to count how many times a method is called."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Decorator to store call history: inputs and outputs """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function """
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))

        return result
    return wrapper


class Cache():
    """ Cache class for cahing with redis """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()


    @call_histroy
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store method which stores data and gives it a unique id for storage """
        self.data = data
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


    def get(self, key: str, fn: Optional[Callable] = None) -> Union[bytes, str, int, None]:
        """ Method to get data by the key """
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value) if fn else value


    def get_str(self, key: str) -> Optional[str]:
        """ Returns the sring version of of the data if it is string """
        return self.get(key, fn=lambda d: d.decode('utf-8'))


    def get_int(self, key: str) -> Optional[int]:
        """ Returns the integer version of of the data if it is number """
        return self.get(key, fn=int)
