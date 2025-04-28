#!/usr/bin/env python3
"""
This module contains a helper function for pagination.
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Returns a tuple of start and end indexes for pagination parameters.
    """
    if page <= 0 or page_size <= 0:
        return (0, 0)

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset


def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
    """
    Returns the page of the dataset based on pagination parameters.
    """

    # Verify that both arguments are integers greater than 0
    assert isinstance(page, int) and page > 0, "page must be a positive integer"
    assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"

    # Get the dataset
    dataset = self.dataset()

    # Calculate start and end indexes
    start, end = index_range(page, page_size)

    # Return empty list if indexes are out of range
    if start >= len(dataset):
        return []

    # Return the appropriate page
    return dataset[start:end]
