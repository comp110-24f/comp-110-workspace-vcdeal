"""Practice with importing/coordinates."""

__author__: str = "730745012"


def get_coords(xs: str, ys: str) -> None:
    "Print the formatted pairs of each character in the two input strings"
    index1: int = 0
    while index1 < len(xs):  # while length of xs is less than index 1
        index2: int = 0  # resets index2 so there are no repeat ys
        while index2 < len(ys):
            print(f"({xs[index1]}, {ys[index2]})")  # prints coordinates
            index2 += 1  # increases index2 in the inner loop
        index1 += 1  # increases index1 in the outer loop
    return None


# doesn't need an 'if __name__ == "__main__" because get_coords isn't called
