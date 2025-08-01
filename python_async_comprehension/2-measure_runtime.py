#!/usr/bin/env python3
"""
Measure execution time of running async_comprehension
4 times in parallel.
"""
from typing import Generator, List
import asyncio
import time
import random

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Run async_comprehension 4 times concurrently and measure the total runtime.

    Returns:
        float: Total runtime in seconds.
    """
    start: float = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end: float = time.time()

    return end - start
