#!/usr/bin/env python3
"""Cache Module"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional


class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """Class Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

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
