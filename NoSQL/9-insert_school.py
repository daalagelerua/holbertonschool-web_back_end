#!/usr/bin/env python3
"""
This module insert a new document in a collection
based on kwargs. (_id is the default primary key for every
collection in mongodb)
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs.
    return the new _id
    """
    if mongo_collection is None:
        return None
    
    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id
