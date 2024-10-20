__author__ = "730745012"

"""Tbh idk what this does"""


def find_and_remove_max(input_list: list[int]) -> int:
    """Find and return the largest number in the list"""
    if input_list == []:  # check if the list is empty before doing anything
        return -1
    largest_num: int = input_list[0]  # largest number is the first value in the list
    largest_idx: int = 0  # start index at the first value in the list
    idx: int = 1  # start the index for the while loop at 1
    while idx < len(input_list):
        if input_list[idx] > largest_num:
            largest_num = input_list[idx]
            largest_idx = idx
            input_list.pop(largest_idx)  # pop the element at largest_idx
    return largest_num  # return the largest number
