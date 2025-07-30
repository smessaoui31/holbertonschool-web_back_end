#!/usr/bin/env python3
"""Module that measures average runtime of wait_n."""

import time
import asyncio
from concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time per coroutine for wait_n.

    Args:
        n (int): Number of coroutines.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        float: Average runtime per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
