def find132pattern(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    stack = []
    temp = None
    for num in nums[::-1]:
        if num < temp:
            return True
        else:
            while stack and num > stack[-1]:
                temp = stack.pop()
        stack.append(num)
    return False


print find132pattern([-1, 3, 2, 0])
