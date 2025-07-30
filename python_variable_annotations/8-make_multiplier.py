#!/usr/bin/env python3
"""Module that provides a function to create multiplier functions."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]:
        A function that takes a float and returns the product.
    """
    def multiply(n: float) -> float:
        return n * multiplier

    return multiply
