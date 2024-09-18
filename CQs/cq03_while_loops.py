"""Practice using while loops."""

__author__: str = "730745012"


def num_instances(phrase: str, search_char: str) -> int:
    """Returns the count of occurances of search_char in phrase"""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if search_char == phrase[index]:
            count = count + 1
        index = index + 1
    return count


num_instances(phrase="Hello", search_char="H")
