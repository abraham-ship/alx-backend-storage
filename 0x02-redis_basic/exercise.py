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
