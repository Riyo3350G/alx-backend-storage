#!/usr/bin/env python3
"""web module"""
import requests
import redis
from functools import wraps


redis = redis.Redis()


def count_access(fn: callable) -> callable:
    """count access decorator"""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """wrapper function for decorator"""
        redis.incr("count:{}".format(fn.__qualname__))
        return fn(*args, **kwargs)
    return wrapper


@count_access
def get_page(url: str) -> str:
    """function that returns the HTML content of a URL"""
    response = requests.get(url)
    return response.text
