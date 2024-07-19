#!/usr/bin/env python3
from pymongo import MongoClient
"""
Script provides some stats about Nginx logs stored in MongoDB
"""


def nginx_log_stats():
    """
    This function does some MongoDB queries
    """
    ''' Connecting to the MongoDB server'''
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    all_documents = collection.count_documents({})
    print(f'{all_documents} logs')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print("Methods:")

    for method in methods:
        count = collection.count_documents({'method': method})
        print(f'\tmethod {method}: {count}')

    status_check = collection.count_documents({
        'method': 'GET',
        'path': '/status'
    })

    print(f'{status_check} status check')


if __name__ == "__manin__":
    nginx_log_stats()
