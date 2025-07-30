#!/usr/bin/env python3
"""
Module that provides a function returning
element lengths from an iterable.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing elements and their lengths.

    Args:
        lst (Iterable[Sequence]): An iterable of sequence-type elements.

    Returns:
        List[Tuple[Sequence, int]]:
        A list where each tuple contains the element and its length.
    """
    return [(i, len(i)) for i in lst]
