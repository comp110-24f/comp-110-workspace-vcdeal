"""Creating my own Wordle game!"""

__author__: str = "730745012"


def input_guess(length: int) -> str:
    """Asks user to input a word"""
    word: str = input(f"Enter a {length} character word.")  # asks user for a word
    while len(word) != length:  # if the word length does equal input length
        word = input(
            (f"Error: That wasn't {length} chars! Try again:")
        )  # asks user to try again
    return word


def contains_char(secret_word: str, char: str) -> bool:
    """See if a character in given word matches a character in the secret word."""
    assert len(char) == 1
    index: int = 0  # starts with an index of 0
    while index < len(secret_word):  # must be less than the secret word length
        if char == secret_word[index]:
            return True  # returns True if the character is in the word
        index += 1
    return False  # returns False if the character isn't in the word


def emojified(guess: str, secret: str) -> str:
    """Comparing the guessed to the secret word"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0  # starts with index of 0
    result: str = ""  # starts with a blank result
    while index < len(secret):
        if (
            guess[index] == secret[index]
        ):  # if the letters match in the secret and the guessed word
            result += GREEN_BOX  # add a green box to the result
        elif contains_char(
            secret_word=secret, char=guess[index]
        ):  # if the letters don't match but the char is in the word
            result += YELLOW_BOX  # add a yellow box to the result
        else:  # if the character isn't in the word
            result += WHITE_BOX  # add a white box to the result
        index += 1
    return result


def main(secret: str) -> None:
    """The entrypoint of the program"""
    turns: int = 1  # tracks number of turns the user has used
    game: bool = False  # tracks if the user has won or not
    while (
        turns <= 6 and game is False
    ):  # allows up to 6 turns if the user has not already won
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(
            length=len(secret)
        )  # prompts the user for a guess and stores the answer
        print(
            emojified(guess=guess, secret=secret)
        )  # prints results of emojified using the user's guess as an arg
        if guess == secret:  # checks if the guess matches the secret word
            game = True  # game has been won
        else:
            turns += 1
    if game is True:  # if the game has been won
        print(f"You won in {turns}/6 turns!")  # prints win message
    else:  # if the game has been lost
        print("X/6 - Sorry, try again tomorrow!")  # prints try-again message


if __name__ == "__main__":
    main(secret="codes")
