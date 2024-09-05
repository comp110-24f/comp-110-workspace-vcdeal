"""CQ00 - Practice Writing Functions"""

__author__ = "730745012"


def mimic(message: str) -> str:
    """Returns a message back to me."""
    return message


def main() -> None:
    """Prints the result of calling 'mimic'."""
    print(mimic(message=input("What is your message?")))
    return None


if __name__ == "__main__":
    main()
