#!/usr/bin/env python3
"""NGINX Log stats module"""
import pymongo


def nginx_logs_stats(nginx_collection):
    """function that provides some stats about Nginx logs stored in MongoDB"""
    totalCollection = nginx_collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    counts = [nginx_collection.count_documents({"method": m}) for m in methods]
    status = nginx_collection\
        .count_documents({"method": "GET", "path": "/status"})
    print(f"{totalCollection} logs")
    print("Methods:")
    for m, c in zip(methods, counts):
        print(f"\tmethod {m}: {c}")
    print(f"{status} status check")
    return None


if __name__ == "__main__":
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    nginx_logs_stats(nginx_collection)
