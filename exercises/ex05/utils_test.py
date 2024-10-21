"""Defining unit tests for list utility functions."""

__author__ = "730645012"

from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_edge_case() -> None:
    """Testing only_evens on an empty list"""
    assert only_evens([]) == []


def test_only_evens_use_case_mutate() -> None:
    """Tests that function mutates the list correctly."""
    a: list[int] = [1, 2, 3, 4]
    assert only_evens(a) == [2, 4]


def test_only_evens_use_case_return() -> None:
    """Tests if the function returns correct output"""
    a: list[int] = [2, 2, 2]
    assert only_evens(a) == [2, 2, 2]


def test_sub_edge_case() -> None:
    """Testing sub with an empty list"""
    assert sub([], 1, 2) == []


def test_sub_use_case_modify() -> None:
    """Testing sub doesn't modify list input"""
    a: list[int] = [1, 2, 3, 4]
    sub(a, 0, 2)
    assert a == [1, 2, 3, 4]


def test_sub_use_case_return() -> None:
    """Testing sub returns expected output"""
    a: list[int] = [1, 2, 3, 4]
    assert sub(a, 1, 3) == [2, 3]


def test_add_at_index_edge() -> None:
    """"""
