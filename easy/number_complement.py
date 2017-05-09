def find_complement(num):
    return int('0b' + '1' * (len(bin(num)) - 2), 2) ^ num

