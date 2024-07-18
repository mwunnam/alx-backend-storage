#!/usr/bin/env python3
from typing import List, Dict, Any
'''
Retuns a list of school having the specific topic
'''


def schools_by_topic(mongo_collection: Collection, topic: str) -> List[Dict[str, Any]]:

    '''
    Function that retuns a list  of school depending on the
    topic requested
    '''
    schools = mongo_colloection.find({"topics": topic})
    return list(schools)
