def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    buttons = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
        '0': [' ']
    }

    if len(digits) == 0:
        return []

    if len(digits) == 1:
        return buttons[digits[0]]

    def combi(key, combinations):
        combination_new = []
        for i in range(len(buttons[key])):
            for j in range(len(combinations)):
                combination_new.append(combinations[j] + buttons[key][i])
        return combination_new

    combis = combi(digits[1], buttons[digits[0]])

    if len(digits) > 2:
        for d in range(2, len(digits)):
            combis = combi(digits[d], combis)

    return combis

print letterCombinations('234')


