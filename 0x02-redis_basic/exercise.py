#!/usr/bin/env python3
"""Cache Module"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """count calls decorator"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function for decorator"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """call history decorator"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function for decorator"""
        self._redis.rpush("{}:inputs".format(key), str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush("{}:outputs".format(key), str(data))
        return data

    return wrapper


def replay(method: Callable):
    """replay function"""
    key = method.__qualname__
    rd = redis.Redis()
    count = rd.get(key).decode("utf-8")
    inputs = rd.lrange("{}:inputs".format(key), 0, -1)
    outputs = rd.lrange("{}:outputs".format(key), 0, -1)
    print("{} was called {} times:".format(key, count))
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(key, i.decode("utf-8"),
                                     o.decode("utf-8")))


class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """Class Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data method"""
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Optional[Callable] = None):
        """Get Method"""
        data = self._redis.get(key)
        if fn is int:
            return self.get_int(data)
        elif fn is str:
            return self.get_str(data)
        elif callable(fn):
            return fn(data)
        else:
            return data

    def get_int(self, data: bytes) -> int:
        """fun that converts data from bytes to int"""
        return int(data)

    def get_str(self, data: bytes) -> str:
        """func that converts data from bytes to str"""
        return data.decode("utf-8")
