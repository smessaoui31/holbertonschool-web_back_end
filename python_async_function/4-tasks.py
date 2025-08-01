#!/usr/bin/env python3
"""
Module that runs multiple task_wait_random concurrently
and returns results in order of completion.
"""

import asyncio
from typing import List
from tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n (int): Number of tasks to spawn.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: List of delays in order of completion.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        results.append(delay)

    return results
