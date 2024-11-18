"""Practice with recursive functions."""


def factorial(n: int) -> int:
    """Compute factorial of n."""
    # Base Case(s):
    if n == 1 or n == 0:
        return 1
    # Recursive case: n * recursive call with n - 1 as argument
    else:
        return n * factorial(n - 1)  # progressing towards base case (moving towards 0)
