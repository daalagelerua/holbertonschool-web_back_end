#!/usr/bin/env python3
"""
This module returns a list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns a list of school having a specific topic
    """
    if mongo_collection is None:
        return []

    return list(mongo_collection.find({"topics": topic}))
