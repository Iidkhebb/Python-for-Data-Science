import sys


def check_odd_even(num):
    """
    This function checks whether the given number is odd or even.

    Parameters:
    - num: The number to check (as a string).

    Raises:
    - AssertionError: If more than one argument is provided
      or if the argument is not an integer.
    """

    if len(sys.argv) != 2:
        raise AssertionError(
            "AssertionError: more than one argument is provided"
            if len(sys.argv) > 2
            else "AssertionError: argument is not provided"
        )

    try:
        num = int(num)
    except ValueError:
        raise AssertionError("AssertionError: argument is not an integer")

    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    try:
        check_odd_even(sys.argv[1])
    except IndexError:
        pass
    except AssertionError as e:
        print(e)
