#!/usr/bin/python3
"""
This module is an asynchrone generator that produces
random floats between 0 and 10 waiting 1 second between
each number.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    coroutine which loop 10 times
    wait 1 second between each iteration
    yield random float
    """
    for _ in range(10):
        await asyncio.sleep(1)  # wait 1 sec 😴
        yield random.uniform(0, 10)  # yield random number between 0 and 10
