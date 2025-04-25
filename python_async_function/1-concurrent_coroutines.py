#!/usr/bin/env python3
"""
This module wait a random number of seconds n times and returns
a list of all delays with float values in ascending order
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    wait a random number of seconds n times and
    return a list of all delays
    """
    delays = []

    # This will be called when a coroutine ends
    async def append_delay():
        delay = await wait_random(max_delay)
        # every new delay is added to the list as soon as it's done
        delays.append(delay)
        return delay
    # create n tasks of wait_random
    tasks = [append_delay() for _ in range(n)]
    # wait for every task to be done
    await asyncio.gather(*tasks)
    # return the list
    return delays
