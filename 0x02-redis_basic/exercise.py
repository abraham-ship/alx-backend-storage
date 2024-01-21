#!/usr/bin/env python3
'''writing strings to redis'''
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def call_history(method: Callable) -> Callable:
    '''Storing lists'''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{self.__class__.__name__}.{method.__name__}:inputs"
        output_key = f"{self.__class__.__name__}.{method.__name__}:outputs"

        self._redis.rpush(input_key, str(args))

        result = method(self, *args, **kwargs)

        self._redis.rpush(output_key, str(result))

        return result

    return wrapper


def count_calls(f) -> Callable:
    '''decorator for counting function'''
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        key = f"{self.__class__.__name__}.{f.__name__}"
        count = self._redis.incr(key)
        return f(self, *args, **kwargs)
    return wrapper


class Cache:
    '''Redis class'''
    def __init__(self):
        '''store an instance of the Redis client as a private variable'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''generates a random key, stores input data and returns the key'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) ->\
            Union[str, bytes, int, None]:
        '''has callable that data back to desired format'''
        retrieved_data = self._redis.get(key)
        if retrieved_data is not None and fn:
            return fn(retrieved_data)
        return retrieved_data

    def get_str(self, key: str) -> str:
        '''convert to string'''
        return self.get(key, fn=str)

    def get_int(self, key: str) -> int:
        '''convert to integer'''
        return self.get(key, fn=int)
