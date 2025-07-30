#!/usr/bin/env python3
"""
Module that runs multiple coroutines concurrently
and returns results in order of completion.
"""

import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds
    and return the delay.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        float: The delay waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with max_delay
    and return results in order of completion.

    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        List[float]: List of delays in order of completion.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
