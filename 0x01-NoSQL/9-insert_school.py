#!/usr/bin/env python3
"""Insert module"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document in a collection based on kwargs"""
    if not mongo_collection:
        return None
    inseted_doc = mongo_collection.insert_one(kwargs)
    return inseted_doc.inserted_id