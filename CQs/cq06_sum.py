"""Summing the elements of a list using different loops."""

__author__: str = "730745012"


def w_sum(vals: list[float]) -> float:
    """Returns sum of all elements using while loop"""
    idx: int = 0  # tracks index
    sum: float = 0.0  # tracks sum
    while idx < len(vals):
        sum += vals[idx]  # sum of each value at each index
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    "Returns the sum of all elements using for in loop"
    sum: float = 0.0
    for number in vals:
        sum += number  # sum of each number, regardless of index
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Returns the sum of all elements using a for in range() loop"""
    idx: int = 0
    sum: float = 0.0
    for idx in range(len(vals)):  # each index in the range of the length
        sum += vals[idx]  # some of each value at each index in given range
    return sum
