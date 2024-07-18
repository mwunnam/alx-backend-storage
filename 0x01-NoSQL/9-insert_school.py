#!/usr/bin/env python3
from pymongo import MongoClient
"""
Inserting a new document in a collection based on kwargs:
"""


def insert_school(mongo_collection, **kwargs):
    """
    Function inserts a new document into a given collection
    the data is stored in a kwargs
    Returns the id of the object of the inserted document
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document
