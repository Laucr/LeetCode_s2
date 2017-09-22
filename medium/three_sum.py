def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) < 3:
        return []
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        pointer_r = len(nums) - 1
        pointer_l = i + 1
        while pointer_l < pointer_r:
            s = nums[pointer_l] + nums[pointer_r] + nums[i]

            if s < 0:
                pointer_l += 1
            elif s > 0:
                pointer_r -= 1
            else:
                result.append([nums[pointer_l], nums[pointer_r], nums[i]])
                while pointer_l < pointer_r and nums[pointer_l] == nums[pointer_l + 1]:
                    pointer_l += 1
                while pointer_r > pointer_l and nums[pointer_r] == nums[pointer_r - 1]:
                    pointer_r -= 1
                pointer_l += 1
                pointer_r -= 1
    return result


print threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6])
