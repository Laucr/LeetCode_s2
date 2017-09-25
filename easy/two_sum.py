def twoSum(nums, target):
    table = {}
    result = []
    for i in range(0, len(nums)):
        table[nums[i]] = i
    print table
    for i in range(0, len(nums)):
        if table.get(target - nums[i]) is not None and i != table.get(target - nums[i]):
            print table.get(target - nums[i])
            result.append(i)
            result.append(table.get(target - nums[i]))
            break
    result.sort()
    return result


print twoSum([-1, 2, 1, -4], 1)
