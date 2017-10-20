def cal_points(ops):
    """
    :type ops: List[str]
    :rtype: int
    """
    game_stack = []
    for i in ops:
        if i == '+':
            game_stack.append(game_stack[-1] + game_stack[-2])
        elif i == 'C':
            game_stack.pop()
        elif i == 'D':
            game_stack.append(game_stack[-1] * 2)
        else:
            game_stack.append(int(i))

    return sum(game_stack)


print cal_points(["5", "-2", "4", "C", "D", "9", "+", "+"])
