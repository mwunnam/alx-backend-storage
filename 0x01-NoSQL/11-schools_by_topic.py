#!/usr/bin/env python3
from pymongo import MongoClient
"""
Retuns a list of school having the specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Function that retuns a list  of school depending on the
    topic requested
    """
    schools = mongo_colloection.find({"topics": topic})
    return list(schools)
