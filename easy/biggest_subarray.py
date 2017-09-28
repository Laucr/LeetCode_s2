def biggest_sub_array(array):
    if len(array) == 0:
        return [], 0

    now_sum = total_sum = 0
    start = stop = 0
    for i in range(len(array)):
        now_sum += array[i]
        if now_sum > total_sum:
            total_sum = now_sum
        elif now_sum < 0:
            now_sum = 0
            stop = i + 1
    return array[start: stop], total_sum

print biggest_sub_array([-6, 10, -5, -7, -1, -1])
