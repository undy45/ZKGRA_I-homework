from string import ascii_uppercase as alphabet
from string import digits
from typing import List


def generate_polybius_square() -> List[str]:
    square: List[str] = []
    characters = alphabet + digits
    while len(characters) != 0:
        square.append(characters[:6])
        characters = characters[6:]
    return square


def cypher(message: str, square: List[str]) -> str:
    coded_message = ''
    for character in message:
        for row_index, row in enumerate(square):
            if character not in row:
                continue
            coded_message += f'{row_index + 1}{row.index(character) + 1} '
            break
    return coded_message.strip()


if __name__ == '__main__':
    messages = ['ENCRYPTME2DAY', 'ENKHBAYAR']
    square = generate_polybius_square()
    for message in messages:
        print(f'original message: {message}')
        print(f'coded message:    {cypher(message, square)}')
