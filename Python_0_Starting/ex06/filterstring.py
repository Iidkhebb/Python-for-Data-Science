import sys


def filter_string(s, n):
    """
    Filter words from the string s that have a length greater than n.

    Parameters:
    - s: The input string.
    - n: The minimum length for words to be included.

    Returns:
    - A list of words from s that have a length greater than n.
    """
    assert isinstance(s, str) and isinstance(n, int), \
        "AssertionError: the arguments are bad"

    return [word for word in s.split() if len(word) > n]


def main(args):
    try:
        assert len(args) == 3, "AssertionError: the arguments are bad"
        s, n = args[1], args[2]
        n = int(n)
        result = filter_string(s, n)
        print(result)
    except (AssertionError, ValueError):
        print('AssertionError: the arguments are bad')


if __name__ == "__main__":
    main(sys.argv)
