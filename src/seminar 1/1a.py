ORDINAL_A: int = ord("a")
ORDINAL_Z: int = ord("z")
ALPHABET_LENGTH: int = ORDINAL_Z - ORDINAL_A + 1


def code(message: str):
    coded_message = ""
    for character in message:
        reverse_order = ALPHABET_LENGTH - (ord(character) - ORDINAL_A) - 1
        coded_message += chr(reverse_order + ORDINAL_A)
    return coded_message


def code_in_numbers(message: str):
    coded_message = []
    for character in message:
        reverse_order = ALPHABET_LENGTH - (ord(character) - ORDINAL_A) - 1
        coded_message.append(str(reverse_order))
    return " ".join(coded_message)


def decode(coded_message: str):
    return code(coded_message)


if __name__ == '__main__':
    message = "enkhbayar"
    print(f"Original Message: [{message}]")
    coded_message = code(message)
    print(f"Coded message in letters: [{coded_message}]")
    print(f"Coded message in numbers: [{code_in_numbers(message)}]")
    print(f"Decoded message: [{decode(coded_message)}]")

