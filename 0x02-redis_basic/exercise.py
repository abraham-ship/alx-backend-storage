#!/usr/bin/env python3
'''writing strings to redis'''
import redis
import uuid
from typing import Union


class Cache:
    '''Redis class'''
    def __init__(self):
        '''store an instance of the Redis client as a private variable'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''generates a random key, stores input data and returns the key'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        '''has callable that data back to desired format'''
        retrieved_data = self.data.get(key, None)
        if retrieved_data is not None and callable(fn):
            return fn(retrieved_data)
        else:
            return retrieved_data

    def get_str(self, key: str) -> str:
        '''convert to string'''
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        '''convert to integer'''
        return self.get(key, fn=int)
