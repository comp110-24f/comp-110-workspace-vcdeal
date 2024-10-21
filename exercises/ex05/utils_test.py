"""Defining unit tests for list utility functions."""

__author__ = "730645012"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


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


def test_sub_use_case_mutate() -> None:
    """Testing sub doesn't mutate list input"""
    a: list[int] = [1, 2, 3, 4]
    sub(a, 0, 2)
    assert a == [1, 2, 3, 4]


def test_sub_use_case_return() -> None:
    """Testing sub returns expected output"""
    a: list[int] = [1, 2, 3, 4]
    assert sub(a, 1, 3) == [2, 3]


def test_add_at_index_edge() -> None:
    """Testing add_at_index with idx = length of list"""
    a: list[int] = [1, 2, 3, 4]
    add_at_index(a, 5, 4)
    assert a == [1, 2, 3, 4, 5]


def test_add_at_index_mutate() -> None:
    """Tests that the function mutates input correctly"""
    a = [1, 2, 4, 5]
    add_at_index(a, 3, 2)
    assert a == [1, 2, 3, 4, 5]


def test_add_at_index_return() -> None:
    """Checks that the output functions as expected"""
    a = [1]
    add_at_index(a, 2, 1)
    assert a == [1, 2]


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    with pytest.raises(IndexError):
        list1 = [1, 2]
        element = 3
        idx = 4
        add_at_index(list1, element, idx)
        # an IndexError is raised for the case when the add_at_index is given an
        # <index_to_insert_num> that is greater than the length of our <list_object>
