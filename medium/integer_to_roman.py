def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """

    """
    compared with this:
    # Roman to Integer
    # I(1) V(5) X(10) L(50) C(100) D(500) M(1000)
    def romanToInt(s):
    roman_dict = {
        'I': 1, 'i': 1,
        'V': 5, 'v': 5,
        'X': 10, 'x': 10,
        'L': 50, 'l': 50,
        'C': 100, 'c': 100,
        'D': 500, 'd': 500,
        'M': 1000, 'm': 1000
    }
    s_list = list(s)
    n_list = []
    for i in range(0, len(s)):
        n_list.append(roman_dict.get(s_list[i]))
    result = 0
    for i in range(0, len(n_list) - 1):
        if n_list[i] < n_list[i+1]:
            result = -n_list[i] + result
        else:
            result += n_list[i]
    result += n_list[len(n_list) - 1]
    return result
    """

    # Input is guaranteed to be within the range from 1 to 3999.

    M = ["", "M", "MM", "MMM"]
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return M[num/1000] + C[(num % 1000)/100] + X[(num % 100)/10] + I[num % 10]

print intToRoman(1999)
