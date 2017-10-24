def nextGreaterElement(find_nums, nums):
    """
    :type find_nums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """

    # ret = []
    # num_order = {}
    #
    # for i in range(len(nums)):
    #     num_order[nums[i]] = i
    #
    # for i in range(len(find_nums)):
    #     start = num_order[find_nums[i]]
    #     ret.append(-1)
    #     for j in range(start, len(nums)):
    #         if nums[j] > find_nums[i]:
    #             ret.pop()
    #             ret.append(nums[j])
    #             break
    # return ret

    nums_dict = {}
    stack = []
    ret = []
    for num in nums:
        while len(stack) > 0 and stack[-1] < num:
            nums_dict[stack[-1]] = num
            stack.pop()
        stack.append(num)
    for num in find_nums:
        if num in nums_dict:
            ret.append(nums_dict[num])
        else:
            ret.append(-1)
    return ret


print nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
