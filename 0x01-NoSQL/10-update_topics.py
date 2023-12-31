#!/usr/bin/env python3
'''change school topics'''


def update_topics(mongo_collection, name, topics):
    '''change topic of a document based on the name'''
    result = mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
    return result.modified_count
