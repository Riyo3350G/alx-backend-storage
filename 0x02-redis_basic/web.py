#!/usr/bin/env python3
"""web caching module"""
import requests
import redis
from functools import wraps
from typing import Callable


rd = redis.Redis()


def get_page(url: str) -> str:
    """function that returns the HTML content of a URL"""
    html = requests.get(url).text
    if not rd.get(f"count:{url}"):
        rd.set(f"count:{url}", 1)
        rd.setex(f"result:{url}", 10, html)
    else:
        rd.incr(f"count:{url}", 1)
    return html
