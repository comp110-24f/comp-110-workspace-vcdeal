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
    """Generate a list between start index and end index"""
    list_ouput: list[int] = []
    if start_idx < 0:
        start_idx = 0  # overrides a negative start index
    if end_idx > len(list_input):
        end_idx = len(list_input)  # overrides a too-big end index
    if len(list_input) == 0:
        return list_ouput  # if list is empty, return empty list
    for idx in range(start_idx, end_idx):
        list_ouput.append(
            list_input[idx]
        )  # for each idx in given range, add the given value to the output list
    return list_ouput


def add_at_index(list_input: list[int], element: int, idx: int) -> None:
    """Modifies input list to place element at given input"""
    if idx > len(list_input) or idx < 0:
        raise IndexError("Index is out of bounds for the input list")
    list_input.append(0)  # creates spaceholder at end of list to be replaced later
    for x in range(
        len(list_input) - 1, idx, -1
    ):  # range from end of list (ignoring placeholder) to given index, goes backward
        list_input[x] = list_input[
            x - 1
        ]  # shifts each value over one index to the right
    list_input[idx] = element  # adds element to list
