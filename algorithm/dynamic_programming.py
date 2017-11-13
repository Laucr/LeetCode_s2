def number_of_coins(coins, target):
    """
    :param coins: List[int]
    :param target: int
    :return: int
    """

    dp = [i for i in range(target + 1)]

    for i in range(1, target + 1):
        for j in range(len(coins)):
            if i >= coins[j] and dp[i - coins[j]] + 1 < dp[i]:
                dp[i] = dp[i - coins[j]] + 1

    return dp[target]


print number_of_coins([1, 3, 5], 11)
