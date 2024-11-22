"""Practice w/ Recursions."""

from __future__ import annotations


class Node:
    """Class of a Node (idrk what a Node is)."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Init."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of a linked list."""
        rest: str = "TODO"
        # TODO: figure out the rest of the list
        if self.next is None:
            rest = "None"
        else:
            rest = self.next.__str__()  # same as str(self.next)
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(310, None)))


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str."""
    # Base Case: if head is empty
    if head is None:
        return "None"
    else:
        # Recursive Case:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


def last(head: Node) -> int:
    """Return the last value of a non-empty list."""
    # Base Case: when head is the "last" node
    if head.next is None:
        return head.value
    else:
        # Recursive case:
        rest: int = last(head.next)
        return rest


def recursive_range(start: int, end: int) -> Node | None:
    """Build a list recursively from start to end."""
    # Edge Case:
    if start > end:
        raise ValueError("Invalid arguments, start > end.")
    # Base Case:
    if start == end:
        return None
    # Recursive Case:
    else:
        return Node(start, recursive_range(start + 1, end))


def value_at(head: Node | None, index: int) -> int:
    """Returns data of Node stored at the given index."""
    # Edge Case:
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    # Base Case:
    if index == 0:
        return head.value
    # Recursive case:
    return value_at(
        head.next, index - 1
    )  # move to next node and idx gets smaller, gets closer to base case


def max(head: Node | None) -> int:
    """Return max value in linked list."""
    # Edge case:
    if head is None:
        raise ValueError("Cannot call max with None.")
    # Base case:
    if head.next is None:  # if this is the only Node
        return head.value  # this is the largest value
    # Recursive case:
    max_in_list = max(head.next)  # new max of next value
    if head.value > max_in_list:  # if new value is less than head.value
        return head.value
    else:
        return max_in_list  # return new value


def linkify(items: list[int]) -> Node | None:
    """Converts input_list into a list of Nodes."""
    # Edge/Base Case (empty list):
    if items == []:  # true if next Next is None
        return None
    # Recursive Case:
    return Node(
        value=items[0], next=linkify(items[1:])
    )  # creates node with first value, next is recursive starting at next index


def scale(head: Node | None, factor: int) -> Node | None:
    """Multiplies each node value by the factor."""
    # Edge case:
    if head is None:
        return None
    # Base case:
    if head.next is None:  # if next value is empty
        return Node(head.value * factor, None)  # return mult by factor
    else:
        return Node(
            head.value * factor, scale(head.next, factor)
        )  # return value w next also being mul
