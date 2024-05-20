import numpy as np


def square(x: int | float) -> int | float:
    return np.square(x)


def pow(x: int | float) -> int | float:
    return np.power(x, x)


def outer(x: int | float, function) -> object:
    count = x

    def inner() -> float:
        nonlocal count
        count = function(count)
        return count

    return inner
