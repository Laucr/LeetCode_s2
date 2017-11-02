def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    op = ''
    operator = []
    operands = []
    for c in s:
        if c == ' ':
            continue
        if c.isdigit():
            op += c
        else:
            operator.append(c)
            if op:
                operands.append(op)
            op = ''
    if op:
        operands.append(op)
    sign = 1
    stack = []
    print operands
    print operator
    for o in operator:
        if o == '(':
            if stack and stack[-1] == -1:
                sign *= -1
        elif o == ')':
            sign = 1

        elif o == '+':
            stack.append(sign * 1)
        elif o == '-':
            stack.append(sign * -1)
    print stack
    res = int(operands[0])
    for i in range(1, len(operands)):
        res += int(operands[i]) * stack[i - 1]
    return res


print calculate("(3-(2-(5-(9-(4)))))")

#
