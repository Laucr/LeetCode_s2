def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    if len(height) < 2:
        return 0
        # if len(height) == 2:
        #     return min(height[0], height[1])

    # O(n*n)
    # area = 0
    # for i in range(len(height)):
    #     for j in range(i, len(height)):
    #         area = max(area, (abs(i - j)) * min(height[i], height[j]))
    # return area

    # O(n)
    # why this
    # cuz if Left line shorter than Right line then right-shift the L-pointer
    # means discard the container that consist of the L-line and lines shorter than the R-line
    # thus we decrease the useless consumption.

    pointer_l = 0
    pointer_r = len(height) - 1
    area = 0
    while pointer_l < pointer_r:
        area = max(area, (pointer_r - pointer_l) * min(height[pointer_l], height[pointer_r]))
        if height[pointer_l] < height[pointer_r]:
            pointer_l += 1
        else:
            pointer_r -= 1
    return area

print maxArea([1, 1])
