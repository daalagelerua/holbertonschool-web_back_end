#!/usr/bin/env python3
"""
This module wait a random time between 0 and 10 seconds
and returns the number of seconds wited as a float
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait a random time between 0 and max_delay secondes and return that value
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
