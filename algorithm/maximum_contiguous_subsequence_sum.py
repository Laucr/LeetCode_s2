# Finds maximum contiguous sub-sequence sum in a[]
# O(N) on-line algorithm


def max_sub_sum(array):
    max_sum = 0
    this_sum = 0
    for i in array:
        this_sum += i
        if this_sum > max_sum:
            max_sum = this_sum

        elif this_sum < 0:
            this_sum = 0
    return max_sum


print max_sub_sum([4, -3, 5, -2, -1, 2, 6, -2])
