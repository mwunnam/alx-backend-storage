#!/usr/bin/env python3
"""
Script that changes all topic base on the name selected
"""


def update_topics(mongo_collection, name, topics):
    result = mongo_collection.update_Many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result
