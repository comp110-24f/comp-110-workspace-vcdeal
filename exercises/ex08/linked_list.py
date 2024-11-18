"""Practice w/ Recursions."""

from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
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
courses: Node = Node(110, Node(210, Node(301, None)))


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
    # Base Case:
