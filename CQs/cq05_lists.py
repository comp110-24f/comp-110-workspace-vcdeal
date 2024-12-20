"""Mutating functions."""

__author__ = "730745012"


def manual_append(list1: list[int], int: int) -> None:
    """Mutates input by appending int to the list."""
    list1.append(int)  # appends int to list
    return None


def double(list2: list[int]) -> None:
    idx: int = 0
    while idx < len(list2):
        list2[idx] = list2[idx] * 2  # multiplies the value at given index by 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)  # should print doubled values
print(list_2)  # should print doubled values
