#!/usr/bin/env python3
"""
Module that provides a function to return a tuple
from a string and a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple with a string and the square of a number.

    Args:
        k (str): A string key.
        v (Union[int, float]): A number to be squared.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string,
                           and the second is the square of the number.
    """
    return (k, float(v ** 2))
