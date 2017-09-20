"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
# rather difficult
# should be written in C


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    maxval = 0
    label_l = 0
    usedchar = {}

    # 0123456
    # tmmzuxt

    for i in range(len(s)):
        if s[i] in usedchar and label_l <= usedchar[s[i]]:
            label_l = usedchar[s[i]] + 1
        else:
            maxval = max(maxval, i - label_l + 1)

        usedchar[s[i]] = i
        print usedchar, label_l
        print maxval
    return maxval


# lengthOfLongestSubstring("abcabcbb")
lengthOfLongestSubstring("tmmzuxt")
