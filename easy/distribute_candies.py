def distribute_candies(candies):
    candies_d = {}
    for i in candies:
        if i not in candies_d:
            candies_d[i] = 1
        else:
            candies_d[i] += 1
    return min(len(candies) / 2, len(candies_d))

