#!/usr/bin/env python3
"""web module"""
import requests
import redis
from functools import wraps


redis = redis.Redis()


def count_access(fn: callable) -> callable:
    """count access decorator"""
    @wraps(fn)
    def wrapper(url):
        """wrapper function for decorator"""
        redis.incr(f"count:{url}")
        cached_html = redis.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = fn(url)
        redis.setex(f"cached:{url}", 10, html)
        return html
    return wrapper


@count_access
def get_page(url: str) -> str:
    """function that returns the HTML content of a URL"""
    response = requests.get(url)
    return response.text
