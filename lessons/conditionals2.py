"""Practice with conditionals and variabes."""


def less_than_10(num: int) -> None:
    """Tell me if a num is < 10."""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("Small Number")
    else:
        print("Big Number")
    print("Have a nice day!")


# less_than_10(num=5)


def get_weather_report() -> str:
    """Finds out what the weather is."""
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


get_weather_report()
