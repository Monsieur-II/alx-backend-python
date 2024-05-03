#!/usr/bin/env python3
"""Task 8 module."""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""
    def multiply(n: float) -> float:
        """Return the product of a float and multiplier."""
        return n * multiplier
    return multiply
