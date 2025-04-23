#!/usr/bin/env python3
"""
This module create a function that multiplies a float by a given
multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a function that multiplies a float by a given multiplier."""
    def multiply(n: float) -> float:
        return n * multiplier

    return multiply
