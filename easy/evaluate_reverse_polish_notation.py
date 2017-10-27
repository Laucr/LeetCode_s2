def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []

    def calc(op2, op1, operator):
        if operator == '+':
            return op1 + op2
        if operator == '-':
            return op1 - op2
        if operator == '*':
            return op1 * op2
        if operator == '/':
            return int(float(op1) / op2)

    for token in tokens:
        try:
            stack.append(int(token))
        except ValueError:
            stack.append(calc(stack.pop(), stack.pop(), token))

    return stack.pop()


print evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
# print int('-')
# 10 * 6 / (9+3) * (-11) + 17 + 5
