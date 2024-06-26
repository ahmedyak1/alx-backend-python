#!/usr/bin/env python3
""" task 0
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay 
    Args:
        max_delay (int, optional): The max delay in seconds. Defaults to 10.
    Returns:
        float: The delay in seconds.
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
