#!/usr/bin/env python3
"""
Cache module using Redis
"""
import uuid
from functools import wraps
from typing import Any, Callable, Optional, Union

import redis


def count_calls(method: Callable) -> Callable:
    """Count how many times a method of Cache is called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """Increment the call counter then call the original method"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Store the history of inputs and outputs of a method"""
    inputs_key = "{}:inputs".format(method.__qualname__)
    outputs_key = "{}:outputs".format(method.__qualname__)

    @wraps(method)
    def wrapper(self, *args) -> Any:
        """Record inputs and outputs then return the output"""
        self._redis.rpush(inputs_key, str(args))
        output = method(self, *args)
        self._redis.rpush(outputs_key, output)
        return output
    return wrapper


def replay(method: Callable) -> None:
    """Display the history of calls of a particular function"""
    name = method.__qualname__
    client = method.__self__._redis
    count = client.get(name)
    count = int(count) if count else 0
    inputs = client.lrange("{}:inputs".format(name), 0, -1)
    outputs = client.lrange("{}:outputs".format(name), 0, -1)

    print("{} was called {} times:".format(name, count))
    for args, output in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(
            name, args.decode("utf-8"), output.decode("utf-8")))


class Cache:
    """Cache class storing data in Redis"""

    def __init__(self) -> None:
        """Initialize the Redis client and flush the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data under a random key and return the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float, None]:
        """Get data from Redis and convert it with fn if given"""
        data = self._redis.get(key)
        if data is None or fn is None:
            return data
        return fn(data)

    def get_str(self, key: str) -> Optional[str]:
        """Get data from Redis as a UTF-8 string"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Get data from Redis as an integer"""
        return self.get(key, fn=int)
