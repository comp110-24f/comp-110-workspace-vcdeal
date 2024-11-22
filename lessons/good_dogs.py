"""More practice with recursions."""


def all_good(scores: list[dict[str, str]], thresh: int, idx: int) -> bool:
    """Checks if all dogs meet good threshold."""

    is_good: bool = int(scores[idx]["score"]) >= thresh
    is_last: bool = idx + 1 == len(scores)

    if is_good:
        if is_last:  # base case
            return True
        else:  # check next dog
            return all_good(scores, thresh, idx + 1)
    else:
        return False
