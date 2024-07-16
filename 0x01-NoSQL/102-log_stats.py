#!/usr/bin/env python3
"""Improve 12-log_stats.py by adding the top 10 of the most
present IPs in the collection nginx of the database logs"""
from pymongo import MongoClient
from collections import Counter


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

# Get the top 10 most frequent IPs
ip_counts = Counter([doc['ip'] for doc in collection.find({}, {'ip': 1})])
top_ips = ip_counts.most_common(10)

print("IPs:")
for ip, count in top_ips:
    print(f"\t{ip}: {count}")
