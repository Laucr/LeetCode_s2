def maximalRectangle(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if len(matrix) == 0:
        return 0

    row = len(matrix)
    col = len(matrix[-1])

    lines = []
    for r in range(row):
        stack = []
        for c in range(col):
            if matrix[r][c] == '1':
                stack.append(c)
        lines.append(stack)



maximalRectangle(
    [["1", "0", "1", "0", "0"],
     ["1", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "0", "0", "1", "0"]]
)
