"""Practice with importing concatenations."""

__author__: str = "730745012"


def concat(input1: str, input2: str) -> str:
    """Returns the concatenation of two input strs."""
    return input1 + input2


word1: str = "happy"

word2: str = "tuesday"

if __name__ == "__main__":
    print(concat(input1=word1, input2=word2))
