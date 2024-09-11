"""A game similar to Wordle!!"""

__author__: str = "730745012"


def input_word() -> str:
    word: str = input("Enter a 5-letter word: ")  # asks user for a word
    if len(word) == 5:  # checks if the length of the word is 5
        print("'" + word + "'")  # puts apostrophes around the word when printing
        return word
    else:
        print("Error: Word must contain 5 characters.")  # prints error message
        print("'" + word + "'")
        return word


# input_word()


def input_letter() -> str:
    letter: str = input(
        "Enter a single character: "
    )  # prompts user for a single character
    if len(letter) == 1:  # checks if length of letter is one
        print("'" + letter + "'")
        return letter
    else:
        print("Error: Character must be a single character.")  # prints error message
        print("'" + letter + "'")
        return letter


# input_letter()


def contains_char(
    input_word: str, input_letter: str
) -> None:  # takes input_word and input_letter as arguments
    if input_letter == input_word[1]:
        print(input_letter + "found at index 1")
    if input_letter == input_word[2]:
        print(input_letter + "found at index 2")
    if input_letter == input_word[3]:
        print(input_letter + "found at index 3")
    if input_letter == input_word[4]:
        print(input_letter + "found at index 4")
    if input_letter == input_word[5]:
        print(input_letter + "found at index 5")
    return None


# i dont think i did the last part correctly but i am not finished
