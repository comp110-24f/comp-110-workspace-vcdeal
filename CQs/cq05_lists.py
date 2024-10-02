"""Mutating functions."""

__author__ = "730745012"


def manual_append(list: list, int: int) -> None:
    """Mutates input by appending int to the list."""
    list.append(int)  # appends int to list
    return None


def double(list: list) -> None:
    idx: int = 0
    while idx < len(list):
        list[idx] = list[idx] * 2  # multiplies the value at given index by 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)  # should print doubled values
print(list_2)  # should print doubled values
