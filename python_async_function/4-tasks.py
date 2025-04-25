#!/usr/bin/env python3
"""
This module execute task_wait_random n times with a specified delay
"""
import asyncio
from typing import list
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Execute task_wait_random n times with specified max_delay"""
    delays = []
    async def append_delay():
        task = task_wait_random(max_delay)
        delay = await task
        delays.append(delay)
        return delay
    
    tasks = [append_delay() for _ in range(n)]

    await asyncio.gather(*tasks)

    return delays
