#!/usr/bin/env python3
"""Type-annotated function sum_mixed_list which takes a list mxd_list"""


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Return the sum of a list of floats and integers."""
    return sum(mxd_list)
