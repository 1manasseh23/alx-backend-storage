#!/usr/bin/env python3
"""This  a Python script that provides some stats
about Nginx logs stored in MongoDB"""


from pymongo import MongoClient

# Connect to the MongoDB database
client = MongoClient()
db = client['logs']
collection = db['nginx']

# Get the total number of logs
total_logs = collection.count_documents({})
print(f"{total_logs} logs")

# Get the count of each HTTP method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
print("Methods:")
for method in methods:
    count = collection.count_documents({"method": method})
    print(f"\tmethod {method}: {count}")

# Get the count of documents with method=GET and path=/status
status_checks = collection.count_documents(
        {"method": "GET", "path": "/status"}
        )
print(f"{status_checks} status check")
