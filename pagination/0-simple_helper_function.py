#!/usr/bin/env python3
"""
This module contains a helper function for pagination.
"""


def index_range(page, page_size):
    """
    Returns a tuple of start and end indexes for pagination parameters.
    """
    if page <= 0 or page_size <= 0:
        return (0, 0)

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
