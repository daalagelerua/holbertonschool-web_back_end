#!/usr/bin/env python3
"""
This module lists all documents in a collection.
"""


def list_all(mongo_collection):
    """
    lists all documents in a mongodb collection
    """
    if mongo_collection is None:
        return []

    return list(mongo_collection.find())
