#!/usr/bin/env python3
"""
This module returns an asyncio.Task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """take an int max_delay and return an object asyncio.Task"""
    # create a task from wait_random coroutine
    task = asyncio.create_task(wait_random(max_delay))
    return task
