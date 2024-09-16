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


input_word()


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


input_letter()


def contains_char(word = input_word(): str, 

# unsure how to call the function


