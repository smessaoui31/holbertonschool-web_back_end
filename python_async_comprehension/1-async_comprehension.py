#!/usr/bin/env python3
"""Async comprehension to collect values from async_generator."""

from typing import List
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 numbers from async_generator using async comprehension.

    Returns:
        List[float]: List of 10 random float values.
    """
    return [i async for i in async_generator()]
