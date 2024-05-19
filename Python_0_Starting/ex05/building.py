import sys


def character_stats(text):
    """
    Calculate and print the statistics of characters in the given text.

    Parameters:
    - text: The input text string.

    Raises:
    - AssertionError: If more than one argument is provided.
    """
    if text is None or text == "":
        text = input("What is the text to count?\n")

    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    punctuation_count = sum(
        1 for char in text if char in '.,;:!?')
    digit_count = sum(1 for char in text if char.isdigit())
    space_count = sum(1 for char in text if char.isspace())

    total_chars = len(text)

    print(f"The text contains {total_chars} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        character_stats(None)
    else:
        try:
            character_stats(sys.argv[1])
        except AssertionError as e:
            print(e)
