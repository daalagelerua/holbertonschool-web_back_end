#!/usr/bin/env python3
"""
This module is used to return the floor of a float number.

Which is the largest inferior integer (3.7 -> 3 / -1.2 -> 2)
"""
import math


def floor(n: float) -> int:
    """Takes the float number and return it's floor."""
    return math.floor(n)
