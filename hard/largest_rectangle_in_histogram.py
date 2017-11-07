def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    # iterate to last height
    heights.append(0)
    # init stack with minimal value
    stack = [-1]
    res = 0

    for i in range(len(heights)):
        # if height-now smaller than height-stack-top
        while heights[i] < heights[stack[-1]]:
            # height eqs last biggest height
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            # just commit bigger result
            res = max(res, h * w)
        # else push the index into stack
        stack.append(i)
    heights.pop()
    return res


print largestRectangleArea([2, 1, 5, 6, 2, 3])
