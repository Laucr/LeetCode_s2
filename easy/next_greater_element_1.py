def next_greater_element(find_nums, nums):
    ret = []
    for i in range(len(find_nums)):
        for j in range(nums.index(find_nums[i]), len(nums)):
            if nums[j] > find_nums[i]:
                ret.append(nums[j])
                break
            elif j == (len(nums) - 1):
                ret.append(-1)
    return ret


print next_greater_element([4, 1, 2], [1, 3, 4, 2])
