"""Practice with conditionals."""


def less_than_10(num: int) -> None:
    """Tell me if a num is < 10."""
    if num < 10:
        print("Small Number")
    else:
        print("Big Number")
    print("Have a nice day!")


def should_i_eat(hungry: bool) -> None:
    """Tells me whether or not to eat based on hunger."""
    if hungry:  # conditional/boolean expression
        print("Eat some food silly goose!")  # "then" block
    else:
        print("Do your Comp110 homework instead.")
    print("I'm proud of you <3")  # either way, be proud of yourself


def check_first_letter(word: str, letter: str) -> str:
    """Determines if the first character of "word" is "letter"."""
    if word[0] == letter:
        return "Match!"
    else:
        return "No match!"


print(check_first_letter(word="beep", letter="b"))
