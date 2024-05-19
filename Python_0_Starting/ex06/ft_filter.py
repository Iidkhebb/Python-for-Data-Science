def ft_filter(function, iterable):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for
    which function(item) is true. If function is None,
    return the items that are true.
    """
    if function is None:
        return (item for item in iterable if item)
    else:
        return (item for item in iterable if function(item))


def main():
    # Test ft_filter function
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Filter even numbers
    even_numbers = ft_filter(lambda x: x % 2 == 0, numbers)
    print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]

    # Filter odd numbers
    odd_numbers = ft_filter(lambda x: x % 2 != 0, numbers)
    print(list(odd_numbers))   # Output: [1, 3, 5, 7, 9]

    # Filter truthy values (function is None)
    truthy_values = ft_filter(None, [0, '', None, False, 1, 'Hello', True])
    print(list(truthy_values))  # Output: [1, 'Hello', True]


if __name__ == "__main__":
    main()
