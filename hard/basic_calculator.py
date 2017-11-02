def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    result, num, sign = 0, 0, 1
    stack = []
    for c in s:
        if c.isdigit():
            num = num * 10 + (ord(c) - ord('0'))
        elif c == '+':
            result += num * sign
            num, sign = 0, 1
        elif c == '-':
            result += num * sign
            num, sign = 0, -1
        elif c == '(':
            stack.append(result)
            stack.append(sign)
            result, num, sign = 0, 0, 1
        elif c == ')':
            result += num * sign
            result *= stack.pop()
            result += stack.pop()
            num, sign = 0, 1
    result += num * sign
    return result


print calculate("(1+(4+2)-3)+(6+8)")

#
