#!/usr/bin/env python3
"""Module that provides a function to sum a list of float numbers."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Compute and return the sum of a list of floats.

    Args:
        input_list (List[float]): A list of float numbers.

    Returns:
        float: The sum of the numbers in the list.
    """
    return sum(input_list)
