#!/usr/bin/env python3
"""
This module execute task_wait_random n times with a specified delay
"""
import asyncio
from typing import list
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Execute task_wait_random n times with specified max_delay"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delays = []
    # Await in comprehension can be problematic => hence below
    for future in asyncio.as_completed(tasks):
        result = await future
        delays.append(result)

    return delays
