from typing import List
from tabulate import tabulate


def generate_table(modulo: int) -> List[List[str]]:
    result: List[List[str]] = []
    for a in range(1, modulo):
        row = []
        for x in range(1, modulo):
            last_modulo_result = 1
            if len(row) != 0:
                last_modulo_result = row[-1]
            modulo_result = (int(last_modulo_result) * a) % modulo
            row.append(str(modulo_result))
        result.append(row)
    result.insert(0, [str(x) for x in range(1, modulo)])
    for a in range(1, len(result)):
        result[a].insert(0, str(a))
    return result


def determine_values(table: List[List[str]], a: int, x: int) -> int:
    return int(table[a - 1][x - 1])


if __name__ == '__main__':
    numbers = [7]
    for i, number in enumerate(numbers):
        table = generate_table(number)
        print(f'Modulo: {number}')
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        print()
        print()
        values = [(1, 1), (3, 4), (4, 2), (5, 6), (6, 6)]
        for a, x in values:
            print(f"(a, x) = ({a}, {x}), {determine_values(table, a, x)}")
