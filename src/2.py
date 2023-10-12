import string
from time import time


def create_dictionary(alphabet_divider: int) -> str:
    dictionary = string.ascii_lowercase
    first_part, second_part = dictionary[:alphabet_divider], dictionary[alphabet_divider:]
    return first_part[::-1] + second_part[::-1]


def code(message: str, dictionary: str):
    coded_message = ""
    for character in message:
        index = string.ascii_lowercase.index(character)
        coded_message += dictionary[index]
    return coded_message


def code_in_numbers(message: str, dictionary: str):
    coded_message = []
    for character in message:
        index = string.ascii_lowercase.index(character)
        coded_character = dictionary[index]
        coded_message.append(str(string.ascii_lowercase.index(coded_character)))
    return " ".join(coded_message)


def decode(coded_message: str, dictionary: str):
    message = ""
    for character in coded_message:
        index = dictionary.index(character)
        message += string.ascii_lowercase[index]
    return message


def decode_in_numbers(coded_message: str, dictionary: str):
    message = ""
    for index in coded_message.split(' '):
        message += dictionary[int(index)]
    return message


# Elapsed whole time: 0.3970332145690918s
# Elapsed time for one iteration: 3.970332145690918e-06s
if __name__ == '__main__':
    message = "enkhbayar"
    dictionary = create_dictionary(12)
    coded_message = code(message, dictionary)
    coded_message_in_numbers = code_in_numbers(message, dictionary)
    start_time = time()
    print(f"Decoding Table for coding in letters:")
    print(f"Coded message: [{coded_message}]")
    for i in range(len(string.ascii_lowercase)):
        dictionary = create_dictionary(i)
        decoded_message = decode(coded_message, dictionary)
        print(f"Divider: [{i}], decoded message: [{decoded_message}]")
    print()
    print(f"Decoding Table for coding in letters:")
    print(f"Coded message: [{coded_message_in_numbers}]")
    for i in range(len(string.ascii_lowercase)):
        dictionary = create_dictionary(i)
        decoded_message = decode_in_numbers(coded_message_in_numbers, dictionary)
        print(f"Divider: [{i}], decoded message: [{decoded_message}]")

