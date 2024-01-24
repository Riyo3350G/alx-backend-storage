#!/usr/bin/env python3
"""Cache Module"""
import redis
from uuid import uuid4
from typing import Union


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
