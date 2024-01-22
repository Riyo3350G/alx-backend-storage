#!/usr/bin/env python3
"""School by topic module"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """function that returns the list of school having a specific topic"""
    if not mongo_collection:
        return []
    docs = mongo_collection.find({"topics": topic})
    return [doc for doc in docs]
