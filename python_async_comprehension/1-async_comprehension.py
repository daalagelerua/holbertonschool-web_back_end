#!/usr/bin/env python3
"""
This module uses a async comprehension list to collect
values from an async generator.
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    coroutine use async comprehension to collect 10 random
    number from async_generator.
    """
    # async iterable must use 'async for'
    rand_nums = [num async for num in async_generator()]
    return rand_nums
