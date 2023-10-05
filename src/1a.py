ORDINAL_A: int = ord("a")
ORDINAL_Z: int = ord("z")
ALPHABET_LENGTH: int = ORDINAL_Z - ORDINAL_A + 1


def code(message: str):
    coded_message = ""
    for character in message:
        reverse_order = ALPHABET_LENGTH - (ord(character) - ORDINAL_A) - 1
        coded_message += chr(reverse_order + ORDINAL_A)
    return coded_message


def decode(coded_message: str):
    return code(coded_message)


if __name__ == '__main__':
    message = "abcd"
    coded_message = code(message)
    print(coded_message)
    print(code(coded_message))

