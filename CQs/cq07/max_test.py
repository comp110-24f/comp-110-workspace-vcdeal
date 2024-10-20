__author__ = "730745012"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_return_case() -> None:
    """Ensures that find_and_remove_max returns the expected value"""
    a: list[int] = [1, 2, 3]
    assert find_and_remove_max(a) == 3


def test_find_and_remove_max_mutate_case() -> None:
    """Ensures that find_and_remove_max mutates the list"""
    a: list[int] = [1, 2, 3]
    find_and_remove_max(a)
    assert a == [1, 2]


def test_find_and_remove_max_edge_case() -> None:
    """Ensures that find_and_remove_max returns the correct input when
    the list is empty"""
    assert find_and_remove_max([]) == -1
