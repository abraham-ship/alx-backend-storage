#!/usr/bin/env python3
'''using python'''


def list_all(mongo_collection):
    '''function that lists all documents in a collection'''
    docs = list(mongo_collection.find())
    return docs if docs else []
