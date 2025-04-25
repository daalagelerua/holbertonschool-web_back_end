#!/usr/bin/env python3
"""
This module measure the execution time time of wait_n function
"""
wait_n = __import__('1-concurrent_coroutines').wait_n
import asyncio
import time


async def measure_time(n: int, max_delay: int) -> float:
    """measure total execution time of wait_n and return average time"""
    # set starting time
    start_time = time.perf_counter()
    # execute wait_n function
    asyncio.run(wait_n(n, max_delay))
    # set end time
    end_time = time.perf_counter()
    # calculate total execution time
    total_time = end_time - start_time
    # return average time
    return total_time / n
