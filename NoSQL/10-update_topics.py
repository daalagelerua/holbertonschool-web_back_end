#!/usr/bin/env python3
"""
This module changes all topics of a document based
on the name.
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based
    on the name. 
    """
    if mongo_collection is None:
        return

    mongo_collection.update_many(
        {"name: name"},  # filter criteria
        {"$set": {"topics": topics}}  # update operation
    )
