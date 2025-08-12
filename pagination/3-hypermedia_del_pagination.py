#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.
"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset (without header)."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return dataset indexed by original position (0-based)."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {i: truncated_dataset[i]
                                      for i in range(len(truncated_dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a page that is resilient to deletions.

        Args:
            index (int): start index in the indexed dataset (0-based).
            page_size (int): number of items to return.
        """
        if index is None:
            index = 0

        assert isinstance(index, int) and index >= 0, "index must be >= 0"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be > 0"

        indexed = self.indexed_dataset()
        if not indexed:
            return {"index": index, "next_index": None, "page_size": 0, "data": []}

        max_key = max(indexed.keys())
        assert index <= max_key, "index out of range"

        data: List[List] = []
        cursor = index

        # Collect page_size existing rows, skipping deleted indices.
        while len(data) < page_size and cursor <= max_key:
            if cursor in indexed:
                data.append(indexed[cursor])
            cursor += 1

        next_index = cursor if cursor <= max_key else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data,
        }
