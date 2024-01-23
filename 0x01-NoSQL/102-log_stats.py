#!/usr/bin/env python3
"""Log stats module"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    totalCollection = nginx_collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    counts = [nginx_collection.count_documents({"method": m}) for m in methods]
    status = nginx_collection\
        .count_documents({"method": "GET", "path": "/status"})
    print(f"{totalCollection} logs")
    print("Methods:")
    for i in range(len(methods)):
        m = methods[i]
        c = counts[i]
        print(f"\tmethod {m}: {c}")
    print(f"{status} status check")
    print("IPs:")
    ips = nginx_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in ips:
        print(f"\t{ip.get('_id')}: {ip.get('count')}")
