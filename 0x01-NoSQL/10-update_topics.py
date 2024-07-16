#!/usr/bin/env python3
"""This a Python function that changes all topics
of a school document based on the name


def update_topics(mongo_collection, name, topics):
    Updates the topics of a school document
    based on the name.

    mongo_collection.update_one(
        { "name": name },
        { "$set": { "topics": topics } }
    )
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the "topics" field of a school document based on the provided name.
    
    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        name (str): The name of the school to update.
        topics (list of str): The list of new topics to be set.
    
    Returns:
        bool: True if the update was successful, False otherwise.
    """
    try:
        # Update the "topics" field of the document with the provided name
        result = mongo_collection.update_one(
            {"name": name},
            {"$set": {"topics": topics}}
        )
        
        # Check if the update was successful
        return result.modified_count > 0
    except:
        # Return False if the update failed
        return False
