"""Program that will help plan a cozy tea party by calculating the expected cost!"""

__author__: str = "730745012"


def main_planner(guests: int) -> None:
    """This is the entrypoint of the program"""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # prints how many guests there are
    print("Tea Bags: " + str(tea_bags(people=guests)))  # prints the amount of tea bags
    print("Treats: " + str(treats(people=guests)))  # prints the amount of treats
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )  # prints the cost using tea_bags and treats as the arguments for tea_count and treat_count
    return None


def tea_bags(people: int) -> int:
    """Calculates amount of tea bags needed."""
    return people * 2  # 2 teas for every one guest


def treats(people: int) -> int:
    """Calculates amount of treats needed."""
    return int(
        tea_bags(people=people) * 1.5
    )  # calculates 1.5 treats for every 1 tea, need to convert RV into int


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the cost of the tea bags and treats combined."""
    return (tea_count * 0.5) + (
        treat_count * 0.75
    )  # every tea is $0.50, every treat is $0.75


if __name__ == "__main__":
    main_planner(
        guests=int(input("How many guests are attending your tea party?"))
    )  # asks the user how many guests there are
