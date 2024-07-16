#!/usr/bin/env python3
"""This a Python function that inserts a new document
in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection based
    on the provided keyword arguments.
    Args:
        mongo_collection (pymongo.collection.Collection)
        The MongoDB collection object.
        **kwargs: Arbitrary keyword arguments representing
        the fields and values of the new document.
    Returns:
        str: The `_id` of the newly inserted document.
    """

    try:
        # Insert the new document into the collection
        result = mongo_collection.insert_one(kwargs)
        return str(result.inserted_id)
    except:
        # Return None if the insertion failed
        return None
