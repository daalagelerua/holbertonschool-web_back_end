#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a page of the dataset that is deletion-resilient.
        """

        # Get the indexed dataset
        indexed_dataset = self.indexed_dataset()

        # Set default index to 0 if None
        if index is None:
            index = 0

        # Verify index is in valid range
        assert index >= 0, "Index must be a non-negative integer"
        assert index < len(self.dataset()), f"Index out of range: {index}"

        # Collect the data for the current page
        data = []
        current_index = index
        item_count = 0

        while item_count < page_size and current_index < len(self.dataset()):
            # Skip deleted items by moving to the next valid index
            if current_index in indexed_dataset:
                data.append(indexed_dataset[current_index])
                item_count += 1
            current_index += 1

        # Calculate the next index
        next_index = current_index

        # Return hypermedia response
        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
