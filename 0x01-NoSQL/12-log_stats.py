#!/usr/bin/env python3
"""NGINX Log stats module"""
import pymongo

# Connect to MongoDB and get the collection
client = pymongo.MongoClient()
db = client.logs
collection = db.nginx

# Count the number of documents in the collection
totalCollection = collection.count_documents({})

# Count the number of documents with different methods
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
counts = [collection.count_documents({"method": m}) for m in methods]

# Count the number of documents with method=GET and path=/status
status = collection.count_documents({"method": "GET", "path": "/status"})

# Print the output
print(f"{totalCollection} logs")
print("Methods:")
for m, c in zip(methods, counts):
    print(f"\tmethod {m}: {c}")
print(f"{status} status check")