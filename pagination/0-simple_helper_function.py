#!/usr/bin/env python3
"""
Helper function for pagination: calculates start and end indexes.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns the start and end index for a given page.

    Args:
        page (int): Page number (starts at 1).
        page_size (int): Number of items per page.

    Returns:
        Tuple[int, int]: Start index (included) and end index (excluded).
    """
    start: int = (page - 1) * page_size
    end: int = page * page_size
    return (start, end)
