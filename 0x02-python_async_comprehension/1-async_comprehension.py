#!/usr/bin/env python3
'''
Task 1. Async Comprehensions
'''
from typing import List
from importlib import import_module as using
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Task 1. Async Comprehensions
    '''
    return [num async for num in async_generator()]
