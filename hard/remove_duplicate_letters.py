# -*-coding:GBK -*-


def removeDuplicateLetters(s):
    """
    :type s: str
    :rtype: str
    """
    # ʱ�临�Ӷ�Ϊ O(n)
    d = {}
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = 1
        else:
            d[s[i]] += 1

    # ͳ��ÿ���ַ����ֵĴ���

    stack = []
    for c in s:
        d[c] -= 1
        # d[c]�Լ�����ʾ���ַ��Ѿ���������
        if c in stack:
            # ����ȥ��
            continue
        while stack and stack[-1] > c and d[stack[-1]] > 0:
            # ��ջ��Ϊ�գ�ջ���ַ����ڵ�ǰ�ַ�����δ��������ַ�������ջ��Ԫ��
            stack.pop()
        # ���ַ���ջ
        stack.append(c)

    return ''.join(stack)

print removeDuplicateLetters("bcabc")

