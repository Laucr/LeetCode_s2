def removeDuplicateLetters(s):
    """
    :type s: str
    :rtype: str
    """
    d = {}
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = 1
        else:
            d[s[i]] += 1

    stack = []
    for c in s:
        d[c] -= 1
        if c in stack:
            continue
        while stack and stack[-1] > c and d[stack[-1]] > 0:
            stack.pop()
        stack.append(c)

    return ''.join(stack)

print removeDuplicateLetters("bcabc")

