#!/usr/bin/env python3
"""
Listing all document in a collection
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    Function takes a collection and list all the document in it
    returns a list of the document
    """
    all_documents = []
    for document in mongo_collection.find():
        all_documents.append(document)

    return all_documents
