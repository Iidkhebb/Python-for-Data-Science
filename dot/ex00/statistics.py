import numpy as np
from typing import Any


def ft_mean(array: np.array):
    try:
        mean = np.mean(array)
        print(f"mean : {mean}")
    except Exception as e:
        print(f"Error : {e}")


def ft_median(array: np.array):
    try:
        median = int(np.median(array))
        print(f"mean : {median}")
    except Exception as e:
        print(f"Error : {e}")


def ft_quartile(array: np.array):
    try:
        quartile_25 = np.percentile(array, 25)
        quartile_75 = np.percentile(array, 75)
        print(f"quartile : {[quartile_25, quartile_75]}")
    except Exception as e:
        print(f"Error : {e}")


def ft_std(array: np.array):
    try:
        std = np.std(array)
        print(f"std : {std}")
    except Exception as e:
        print(f"Error : {e}")


def ft_var(array: np.array):
    try:
        var = np.var(array)
        print(f"var : {var}")
    except Exception as e:
        print(f"Error : {e}")


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    if kwargs is None or len(args) == 0:
        print("ERROR\n" * len(kwargs.values()), end="")
        return

    array = np.array(args)
    dict_n = {
        "var": ft_var,
        "median": ft_mean,
        "std": ft_std,
        "quartile": ft_quartile,
        "mean": ft_mean,
    }

    for x in kwargs.values():
        try:
            dict_n[x](array)
        except KeyError:
            pass
        except Exception:
            print("ERROR")
