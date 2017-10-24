def nextGreaterElements(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    length = len(nums)
    ret = [-1] * length
    stack = []

    for i in range(2 * length):
        num = nums[i % length]
        while len(stack) > 0 and nums[stack[-1]] < num:
            ret[stack[-1]] = num
            stack.pop()
        if i < length:
            stack.append(i)

    return ret


print nextGreaterElements([100, 1, 11, 1, 120, 111, 123, 1, -1, -100])
