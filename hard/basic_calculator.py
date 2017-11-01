def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    op = ''
    operator = []
    calc = []
    for c in s:
        if c == ' ':
            continue
        if c.isdigit():
            op += c
        else:
            operator.append(c)
            if op:
                calc.append(op)
            op = ''
    if op:
        calc.append(op)

    stack = []
    sign = 0
    for p in operator:
        if p == '+':
        elif p == '-':
        elif p == '(':
        elif p == ')':

    print operator
    print calc

calculate("(1+(4+5+2)-3)+(6+8)")
