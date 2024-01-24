#!/usr/bin/env python3
"""web caching module"""
from functools import wraps
from typing import Callable

import redis
import requests

store = redis.Redis()


def data_cacher(method: Callable) -> Callable:
    ''' data_cacher '''
    @wraps(method)
    def wrapper(url) -> str:
        '''wrapper function for decorator'''
        store.incr(f'count:{url}')
        output = store.get(f'cached:{url}')

        if output:
            return output.decode('utf-8')

        output = method(url)
        store.setex(f'cached:{url}', 10, output)
        return output

    return wrapper


@data_cacher
def get_page(url: str) -> str:
    ''' get_page: function that returns html content '''
    return requests.get(url).text
