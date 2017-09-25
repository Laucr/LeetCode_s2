def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    if len(nums) < 3:
        return []
    nums.sort()
    result = {}

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        pointer_r = len(nums) - 1
        pointer_l = i + 1
        while pointer_l < pointer_r:
            s = nums[pointer_l] + nums[pointer_r] + nums[i]
            b = abs(nums[pointer_l] + nums[pointer_r] + nums[i] - target)
            result[s] = b
            if s < target:
                pointer_l += 1
            elif s > target:
                pointer_r -= 1
            else:
                while pointer_l < pointer_r and nums[pointer_l] == nums[pointer_l + 1]:
                    pointer_l += 1
                while pointer_r > pointer_l and nums[pointer_r] == nums[pointer_r - 1]:
                    pointer_r -= 1
                pointer_l += 1
                pointer_r -= 1
    print result
    dis = result.values()[0]
    res = result.keys()[0]
    for i in result:
        if result[i] < dis:
            dis = result[i]
            res = i
    return res

print threeSumClosest([1,1,1,0], -100)