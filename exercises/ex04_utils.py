"""Exercises with lists."""

__author__ = "730745012"


def all(input: list[int], given_int: int) -> bool:
    """Indicates if the ints in the list match the given list"""
    idx: int = 0  # variable that tracks index
    if len(input) == 0:
        return False
    while idx < len(input):  # idx must be less than length
        if input[idx] != given_int:  # if it doesnt equal given_int
            return False
        else:
            idx += 1  # continue
    return True  # if fn doesnt return False than it is True


def max(input: list[int]) -> int:
    """Identifies highest value in a list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    high_num: int = input[0]  # sets first value as highest num
    idx: int = 1  # starts counting index at 1
    while idx < len(input):
        if input[idx] > high_num:  # if next value is greater than first value
            high_num = input[idx]  # high_num gets replaced
        idx += 1
    return high_num


def is_equal(input1: list[int], input2: list[int]) -> bool:
    """Sees if two lists have equal values"""
    idx: int = 0
    while idx < len(input1):
        if (
            input1[idx] == input2[idx]
        ):  # if value of input 1 is equal to value of input 2
            idx += 1
        else:
            return False
    return True


def extend(input1: list[int], input2: list[int]) -> None:
    """Appends a list by adding a second list's values"""
    idx: int = 0
    while idx < len(input2):
        input1.append(input2[idx])
        idx += 1
