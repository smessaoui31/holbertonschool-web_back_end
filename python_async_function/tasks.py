#!/usr/bin/env python3
"""Module that provides a function returning an asyncio Task."""

import asyncio
from basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio Task for wait_random with the given max_delay.

    Args:
        max_delay (int): Maximum delay for the coroutine.

    Returns:
        asyncio.Task: An asyncio Task object wrapping wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))
