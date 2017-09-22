
"""
Manacher's Algorithm used a array Len[i] the radius of the palindrome string with the centre T[i].
E.C. the longest palindrome string is T[l,r] then Len[i] = r - i + 1

original string _S_: a a a b a
add separator   _T_: # a # a # a # b # a #
0 1 2 3 4 5 6 7 8 9 0
# a # a # a # b # a #
1 2 3 4 3 2 1 4 1 2 1

and obviously(??) Len[i] - 1 equals the length of the palindrome reflect to the original string.
so get the Len[i] equals to get the palindrome string.

"""


def manacher(s):
    """
    :type s: str
    :rtype: str
    """
    string_t = '@#' + '#'.join(list(s)) + '#$'
    len_str_t = 2 * len(s) + 1

    point_right_most = 0
    palindrome_len = 0      # Len[i]
    point_longest_centre = 0
    length = [0] * len_str_t
    for i in range(1, len_str_t):
        if point_right_most > i:
            length[i] = min(point_right_most - i, length[2 * point_longest_centre - i])
        else:
            length[i] = 1
        while string_t[i - length[i]] == string_t[i + length[i]]:
            length[i] += 1
        if length[i] + i > point_right_most:
            point_right_most = length[i] + i
            point_longest_centre = i
        if palindrome_len < length[i]:
            palindrome_len = length[i]
            point_longest_centre = i
        # palindrome_len = max(palindrome_len, length[i])

    return palindrome_len - 1
print manacher("abcbd")
