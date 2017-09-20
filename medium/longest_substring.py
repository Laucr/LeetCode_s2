"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    stack = ""
    i = 0
    maxval = 0
    while i < len(s):
        if s[i] not in stack:
            stack += s[i]
            i += 1
            maxval = max(maxval, len(stack))
        else:
            maxval = max(maxval, len(stack))
            label_l = i - len(stack) + 1
            i = label_l
            stack = ""
    return maxval

# 0123
# dvdf
# d
# dv
#  v
#  vd
#  vdf

    # start = maxLength = 0
    # usedChar = {}
    #
    # for i in range(len(s)):
    #     if s[i] in usedChar and start <= usedChar[s[i]]:
    #         start = usedChar[s[i]] + 1
    #     else:
    #         maxLength = max(maxLength, i - start + 1)
    #
    #     usedChar[s[i]] = i
    #     print usedChar
    #
    # return maxLength

print lengthOfLongestSubstring("abcabcbb")
