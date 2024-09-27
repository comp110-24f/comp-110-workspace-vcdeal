"""Practice with importing coordinates."""

__author__: str = "730745012"


def get_coords(xs: str, ys: str) -> None:
    "Print the formatted pairs of each character in the two input strings"
    index1: int = 0
    while index1 < len(xs):
        index2: int = 0
        print(f"({xs[index1]}, {ys[index2]})")
        index1 += 1
        while index2 < len(ys):
            index2 += 1
            print(f"({xs[index1]}, {ys[index2]})")
