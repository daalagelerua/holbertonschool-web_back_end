#!/usr/bin/env python3
"""
This module measure how long it takes to execute 4 times
async_comprehension concurently.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    coroutine execute 4 times async_comprehension
    and measure total execution time.
    """

    start_time = time.perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )

    end_time = time.perf_counter()

    return end_time - start_time
