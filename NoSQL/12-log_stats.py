#!/usr/bin/env python3
"""
Python script that provides stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def nginx_stats():
    """
    Provides statistics about nginx logs stored in MongoDB
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Access the logs database and nginx collection
    nginx_collection = client.logs.nginx

    # Get total number of logs
    total_logs = nginx_collection.count_documents({})

    # Get count for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}

    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        method_counts[method] = count

    # Get count for status check (method=GET, path=/status)
    status_check_count = nginx_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })

    # Display the results
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"    method {method}: {method_counts[method]}")
    print(f"{status_check_count} status check")

    if __name__ == "__main__":
        nginx_stats()
