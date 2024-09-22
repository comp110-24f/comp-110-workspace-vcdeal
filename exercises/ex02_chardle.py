"""A game similar to Wordle!!"""

__author__: str = "730745012"


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")  # asks user for a word
    if len(word) == 5:  # checks if the length of the word is 5
        return word
    else:
        print("Error: Word must contain 5 characters.")  # prints error message
        exit()  # exits code if there are too many characters in word
        return word


def input_letter() -> str:
    letter: str = input(
        "Enter a single character: "
    )  # prompts user for a single character
    if len(letter) == 1:  # checks if length of letter is one
        return letter
    else:
        print("Error: Character must be a single character.")  # prints error message
        exit()  # exits code if there are too many characters in letter
        return letter


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)  # tells user its searching
    count: int = 0  # new variable count
    if word[0] == letter:
        print(
            letter + " found at index 0"
        )  # prints that the letter is found at index 0
        count = count + 1  # adds one to the count if its true
    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1
    if count == 0:
        print(
            "No instances of " + letter + " found in " + word
        )  # prints that there is no instances if count = 0
    else:
        print(
            str(count) + " instances of " + letter + " found in " + word
        )  # prints the amount of counts
    return None


def main() -> None:
    contains_char(
        word=input_word(), letter=input_letter()
    )  # calls the contains_char function
    return None


if __name__ == "__main__":
    main()
