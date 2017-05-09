def hamming_distance(x, y):
    xor = bin(x ^ y)[2:]
    return reduce(lambda a, b: a + b, map(int, xor))

print hamming_distance(1, 4)
