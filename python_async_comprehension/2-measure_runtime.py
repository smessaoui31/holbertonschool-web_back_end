#!/usr/bin/env python3
"""
Measure execution time of running async_comprehension
4 times in parallel.
"""

import asyncio
import time
from 1-async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Run async_comprehension 4 times concurrently and measure the total runtime.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time