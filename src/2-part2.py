from string import ascii_lowercase as alphabet
from typing import List


def ceaser_cypher(message: str, encryption_key: int) -> str:
    coded_message = ''
    for character in message:
        new_index = (alphabet.index(character) + encryption_key) % len(alphabet)
        coded_message += alphabet[new_index]
    return coded_message


def decrypt_ceaser_cypher(message: str, encryption_key: int) -> str:
    coded_message = ''
    for character in message:
        new_index = (alphabet.index(character) - encryption_key) % len(alphabet)
        coded_message += alphabet[new_index]
    return coded_message


def generate_decryption_table(coded_message: str) -> List[str]:
    decryption_table: List[str] = []
    for encryption_key in range(1, len(alphabet)):
        decryption_table.append(decrypt_ceaser_cypher(coded_message, encryption_key))
    return decryption_table


if __name__ == '__main__':
    encryption_key = 10
    message = 'undy'
    message = message.lower()
    print(f'original message: [{message}]')
    coded_message = ceaser_cypher(message, encryption_key)
    print(f'coded message: [{coded_message}]')
    decryption_table = generate_decryption_table(coded_message)
    print('decryption table:')
    print()
    for i, decrypted_message in enumerate(decryption_table):
        print(f'encryption key: {i + 1}, decrypted message: {decrypted_message}')
