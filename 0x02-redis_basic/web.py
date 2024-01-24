#!/usr/bin/env python3
"""web module"""
import requests
import redis
from functools import wraps
from typing import Callable


redis = redis.Redis()


def count_access(method: Callable) -> Callable:
    """count access decorator"""
    @wraps(method)
    def wrapper(url) -> str:
        """wrapper function for decorator"""
        redis.incr("count:{}".format(url))
        cached_html = redis.get("cached:{}".format(url))
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        redis.setex("cached:{}".format(url), 10, html)
        return html
    return wrapper


@count_access
def get_page(url: str) -> str:
    """function that returns the HTML content of a URL"""
    response = requests.get(url)
    return response.text
