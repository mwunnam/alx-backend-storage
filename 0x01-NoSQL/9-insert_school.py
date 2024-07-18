#!/usr/bin/env python3
'''
Inserts a new document in a collection with kwargs
'''


def insert_school(mongo_collection, **kwargs):
    '''Inserts a new document in a collection.
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
