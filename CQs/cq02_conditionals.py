"""Practice with Conditionals, Local Variables, and User Input"""

__author__: str = "730745012"


def guess_a_number() -> None:
    secret: int = 7
    response_number: int = int(input("Guess a number: "))
    print("Your guess was " + str(response_number))
    if response_number == secret:
        print("You got it!")
    if response_number < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    if response_number > secret:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
