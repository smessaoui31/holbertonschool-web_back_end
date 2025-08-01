#!/usr/bin/env python3
"""Module that provides an async function to wait for a random"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay and return the delay
    Args :
        max_delay (int): The maximum number of seconds to wait

    Returns:
        float: The random delay that was waited
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
