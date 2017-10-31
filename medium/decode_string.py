def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    stack = []
    num = []
    counter = 0
    substr = ''
    multi = ''

    for c in s:
        if c == '[':
            num.append(counter)
            counter = 0
            continue
        if c == ']':
            counter = 0
            while not stack[-1].isdigit():
                substr += stack.pop()
            n = int(num.pop())

            print substr
            while n:
                multi += stack.pop()
                n -= 1
            stack.append(int(multi[::-1]) * substr)
            substr = ''
            multi = ''
        else:
            if c.isdigit():
                counter += 1
            stack.append(c)

    return ''.join(stack[::-1])[::-1]


print decodeString("3[a2[c]]")

