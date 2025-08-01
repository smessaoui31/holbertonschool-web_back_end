#!/usr/bin/env python3
"""Async comprehension to collect values from async_generator."""

from typing import Generator, List
import random
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 numbers from async_generator using async comprehension.

    Returns:
        List[float]: List of 10 random float values.
    """
    result: List[float] = [x async for x in async_generator()]
    return result
