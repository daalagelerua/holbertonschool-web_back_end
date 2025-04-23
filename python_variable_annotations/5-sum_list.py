#!/usr/bin/env python3
"""
This module is used to calculate the sum of a list of floating
point numbers.

Using built-in function sum().
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Calculate the sum of a list of float numbers."""
    return float(sum(input_list))
