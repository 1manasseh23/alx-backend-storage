#!/usr/bin/env python3
"""This Create a Cache class. In the __init__ method,
store an instance of the Redis client as a private
variable named _redis (using redis.Redis()) and flush
the instance using flushdb.
Create a store method that takes a data argument and
returns a string. The method should generate a random
key (e.g. using uuid), store the input data in Redis
using the random key and return the key.
Type-annotate store correctly. Remember that data can
be a str, bytes, int or float
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Create keys for inputs and outputs
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        # Normalize inputs and append to the inputs list in Redis
        self._redis.rpush(inputs_key, str(args))

        # Call the original method to get the output
        output = method(self, *args, **kwargs)

        # Append the output to the outputs list in Redis
        self._redis.rpush(outputs_key, output)

        return output
    return wrapper

"""
def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Get the qualified name of the method
        key = method.__qualname__
        # Increment the count in Redis
        current_count = self._redis.incr(key)
        # Call the original method
        return method(self, *args, **kwargs)
    return wrapper
"""

class Cache:
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history # @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self, key: str, fn: Optional[Callable] = None
            ) -> Optional[Union[str, bytes, int, float]]:
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        return self.get(key, fn=int)
