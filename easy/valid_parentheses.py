def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    # ()[]{}
    def dum_method(parentheses):
        stack = ' '
        for i in parentheses:
            if i == '(' or i == '[' or i == '{':
                stack += i
            elif i == ')':
                if stack[-1] != '(':
                    return False
                else:
                    stack -= i
            elif i == ']':
                if stack[-1] != '[':
                    return False
                else:
                    stack -= i
            elif i == '}':
                if stack[-1] != '{':
                    return False
                else:
                    stack -= i
        if stack != ' ':
            return False
        return True

    def clever_method(parentheses):
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for i in parentheses:
            if i in pairs.values():
                stack.append(i)
            else:
                try:
                    if stack.pop() != pairs[i]:
                        return False
                except Exception:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
    return clever_method(s)
    # return dum_method(s)
print isValid("([)]")
