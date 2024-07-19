#!/usr/bin/env python3
'''
Retuns a list of school having the specific topic
'''


def schools_by_topic(mongo_collection, topic):
    '''
    Function that retuns a list  of school depending on the
    topic requested
    '''
    return list(mongo_collection.find({"topics": topic}))
