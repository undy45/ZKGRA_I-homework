if __name__ == '__main__':
    values = [(0b1011, 0b0110, 0b0100), (0b0101, 0b1110, 0b1101)]
    for a, b, c in values:
        print(f"a: {bin(a)}")
        print(f"b: {bin(b)}")
        print(f"c: {bin(c)}")
        print(f"result: {bin(a ^ b ^ c ^ a ^ b)}")
        print()
