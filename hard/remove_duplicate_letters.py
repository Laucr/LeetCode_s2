# -*-coding:GBK -*-


def removeDuplicateLetters(s):
    """
    :type s: str
    :rtype: str
    """
    # 时间复杂度为 O(n)
    d = {}
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = 1
        else:
            d[s[i]] += 1

    # 统计每个字符出现的次数

    stack = []
    for c in s:
        d[c] -= 1
        # d[c]自减，表示此字符已经遍历过了
        if c in stack:
            # 用来去重
            continue
        while stack and stack[-1] > c and d[stack[-1]] > 0:
            # 当栈不为空，栈顶字符大于当前字符，且未遍历完该字符，弹出栈顶元素
            stack.pop()
        # 将字符入栈
        stack.append(c)

    return ''.join(stack)

print removeDuplicateLetters("bcabc")

