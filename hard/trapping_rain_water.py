def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    stack = []
    start = 0
    total = 0
    for h in height:
        if not stack:
            if h > 0:
                stack.append(h)
                start = stack[-1]
        else:
            if h < start:
                stack.append(h)
            else:
                while stack[-1] < start:
                    total += start - stack.pop()
                stack.append(h)
                start = stack[-1]
    print stack

    return total


he = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print trap(he)
