"""Code for implementing lists utility functions."""

__author__ = "730745012"


def only_evens(list_input: list[int]) -> list[int]:
    """Takes given list and returns the even values"""
    list_output: list[int] = []  # creates new list to return even values
    idx: int = 0
    while idx < len(list_input):
        if list_input[idx] % 2 == 0:  # if the remainder of the value is 0
            list_output.append(list_input[idx])  # adds value to output
        idx += 1
    return list_output


def sub(list_input: list[int], start_idx: int, end_idx: int) -> list[int]:
    