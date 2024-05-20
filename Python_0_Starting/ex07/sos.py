import sys


def encrypt(string: str) -> str:
    MORSE_CODE_DICT = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        ",": "--..--",
        ".": ".-.-.-",
        "?": "..--..",
        "/": "-..-.",
        "-": "-....-",
        "(": "-.--.",
        ")": "-.--.-",
        " ": "/ ",
    }

    cipher = ""
    for letter in string.upper():
        if letter in MORSE_CODE_DICT:
            cipher += MORSE_CODE_DICT[letter] + " "
        else:
            cipher += "/ "

    return cipher.strip()


def check_valid_string(string):
    return all(char.isalpha() or char.isspace() for char in string)


def main():
    try:
        assert len(sys.argv) == 2, "AssertionError: the arguments are bad"
        string = sys.argv[1]
        if check_valid_string(string):
            result = encrypt(string)
            print(result)
        else:
            print("AssertionError: the arguments are bad")
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
