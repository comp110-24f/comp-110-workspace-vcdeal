"""Practice with scope"""


def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char removed."""
    copy: str = ""  # Set up empty str to copy values over
    index: int = 0
    while index < len(msg):
        # if the letter is NOT char
        if char != msg[index]:
            # add it to the copy
            copy += msg[index]  # adds non-char to copy
        index += 1  # index = index + msg[index]
    return copy


if __name__ == "__main__":
    word: str = "yoyo"  # GLOBAL variable
    print(remove_chars(msg=word, char="y"))  # with keyword arguments
    # print(remove_chars(word, "o"))  # with positional arguments
