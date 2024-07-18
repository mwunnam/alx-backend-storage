#!/usr/bin/env python3
from pymongo import MongoClient
"""
Script that changes all topic base on the name selected
"""


def update_topics(mongo_collection, name, topics):
    """
    Function changes the topics of a collection's document based
    on the name given
    """
    result = mongo_collection.update_Many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
