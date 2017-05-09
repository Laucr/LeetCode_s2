def matrix_resharp(nums, r, c):
    matrix = [num for row in nums for num in row]
    ret = []
    start = 0
    if r * c == len(matrix):
        step = c
    else:
        return nums
    stop = step
    for row in range(r):
        if not len(matrix[start:stop]):
            break
        ret.append(matrix[start:stop])
        start += step
        stop += step

    return ret


print matrix_resharp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]], 42, 5)
