def find132pattern(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    stack = []
    for num in nums:
        if len(stack) == 0:
            stack.append(num)
        elif len(stack) == 1:
            if stack[-1] > num:
                stack.pop()
            stack.append(num)
        else:
            if stack[-1] > num:
                popped = stack.pop()
                if num > stack[-1]:
                    return True
                else:
                    stack.append(popped)
                    pass
            else:
                stack.pop()
                stack.append(num)

    return False


print find132pattern([8, 10, 4, 6, 5])
