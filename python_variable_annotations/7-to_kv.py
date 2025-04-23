#!/usr/bin/env python3
"""
This module is used to create a tuple with a string and the square
of a float OR int number.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a tuple with a string and the square of a number."""
    return (k, float(v**2))
