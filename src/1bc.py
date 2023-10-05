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


def decode(coded_message: str, dictionary: str):
    message = ""
    for character in coded_message:
        index = dictionary.index(character)
        message += string.ascii_lowercase[index]
    return message


# Elapsed whole time: 0.3970332145690918s
# Elapsed time for one iteration: 3.970332145690918e-06s
if __name__ == '__main__':
    count = 10 ** 5
    start_time = time()
    message = "abcd"
    dictionary = create_dictionary(12)
    coded_message = code(message, dictionary)
    # print(f"original_message: {coded_message}")
    # print(f"coded_message: {coded_message}")
    # print(f"decoded_message: {decode(coded_message, dictionary)}")
    decoded_message = decode(coded_message, dictionary)
    for i in range(count):
        dictionary = create_dictionary(i % 26)
        coded_message = code(message, dictionary)
        decoded_message = decode(coded_message, dictionary)
    end_time = time()
    print(f"Elapsed whole time: {end_time - start_time}s")
    print(f"Elapsed time for one iteration: {(end_time - start_time) / count}s")

