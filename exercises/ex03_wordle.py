"""Creating my own Wordle game!"""


def input_guess(length: int) -> str:
    """Asks user to input a word"""
    word: str = input(f"Enter a {length} letter word.")  # asks user for a word
    while len(word) != length:  # if the word length does equal input length
        word = input(
            (f"Error: That wasn't {length} letters. Try again:")
        )  # asks user to try again
    return word


def contains_char(secret_word: str, char: str) -> bool:
    """See if a character in given word matches a character in the secret word."""
    assert len(char) == 1 # idk what this does really
    index: int = 0 
    while index < len(input_guess()) # how to get input guess here?
