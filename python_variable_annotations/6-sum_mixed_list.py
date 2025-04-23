#!/usr/bin/env python3
"""
This module is used to calculate the sum of a list of integers
and float numbers.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculate the sum of a list of int and float"""
    return float(sum(mxd_lst))
