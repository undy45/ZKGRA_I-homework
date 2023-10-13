numbers = [4, 15, 32]
moduluses = [9, 7, 29]
for i, (number, modulus) in enumerate(zip(numbers, moduluses)):
    result = ['undefined']
    for mod_number in range(1, modulus):
        result.append(str(number % mod_number))
    print(f"2.{i + 1} - vector of number {number} modulus {modulus}: ({', '.join(result)})")
    print()
