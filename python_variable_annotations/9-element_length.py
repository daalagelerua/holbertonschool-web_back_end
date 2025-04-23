#!/usr/bin/env python3
"""
This module provides utility functions for analyzing sequences (like lists,
strings, tuples) and extracting information about their structure and
properties.
"""
from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculate the length of each sequence element in a list."""
    return [(i, len(i)) for i in lst]
