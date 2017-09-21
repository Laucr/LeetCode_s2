def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str"""

    # maybe more efficient way to solve this.

    prefix = ""
    if len(strs) == 0:
        return prefix
    for c in range(len(strs[0])):
        for s in range(len(strs)):
            if c > len(strs[s]) - 1 or strs[0][c] != strs[s][c]:
                return prefix
            if s == len(strs) - 1:
                prefix += strs[0][c]
    return prefix

print longestCommonPrefix(["a"])
