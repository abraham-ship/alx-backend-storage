#!/usr/bin/env python3
'''insert a document'''


def insert_school(mongo_collection, **kwargs):
    '''function to insert a document in a collection'''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
