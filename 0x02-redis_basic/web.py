#!/usr/bin/env python3
"""This implement a get_page function (prototype: def
get_page(url: str) -> str:). The core of the function
is very simple. It uses the requests module to obtain the
HTML content of a particular URL and returns it.
Start in a new file named web.py and do not reuse
the code written in exercise.py
"""
import requests
import redis
import time
from functools import wraps

# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379)


def cache_url_access(method):
    """to defind the wraper function"""
    
    @wraps(method)
    def wrapper(url: str, *args, **kwargs):
        # Track access count
        
        count_key = f"count:{url}"
        redis_client.incr(count_key)

        # Call the original method
        return method(url, *args, **kwargs)

    return wrapper


@cache_url_access
def get_page(url: str) -> str:
    # Check if cached result exists
    
    cache_key = f"cache:{url}"
    cached_result = redis_client.get(cache_key)

    if cached_result:
        return cached_result.decode('utf-8')

    # If not cached, fetch the page
    response = requests.get(url)

    # Store the result in Redis with expiration
    redis_client.setex(cache_key, 10, response.text)

    return response.text


if __name__ == "__main__":
    """The url to fetch from"""
    
    url = "http://httpbin.org/delay/3"  # Alternative slow URL
    print(get_page(url))  # Fetch the page
    time.sleep(1)
    print(get_page(url))  # Fetch from cache
    time.sleep(11)        # Wait for cache to expire
    print(get_page(url))  # Fetch again
