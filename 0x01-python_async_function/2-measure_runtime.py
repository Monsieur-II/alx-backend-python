#!/usr/bin/env python3
"""Measure the runtime"""


import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """measures total execution time for wait_n(n, max_delay)"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.time() - start
    return elapsed_time / n
