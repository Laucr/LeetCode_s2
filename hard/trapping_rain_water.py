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
    if stack and start != stack[-1]:
        end = stack.pop()
        while stack and stack[-1] != start:
            if stack[-1] > end:
                end = stack.pop()
            else:
                total += end - stack.pop()

    return total


print trap([4, 2, 0, 3, 2, 5])
