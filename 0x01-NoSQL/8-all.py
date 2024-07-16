#!/usr/bin/env python3

# 8-all.py

def list_all(mongo_collection):
    """Lists all documents in a collection."""
    return list(mongo_collection.find())  # Return an empty list if no documents
