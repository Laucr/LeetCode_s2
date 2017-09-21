def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    # finally accepted!
    # O(n*n)

    if len(s) < 2:
        return s

    def extend_palindrome_odd(st):
        palindromes = []
        for i in range(len(st)):
            label_l = i - 1
            label_r = i + 1
            palindrome = st[i]
            while label_l >= 0 and label_r < len(st):
                if st[label_l] == st[label_r]:
                    palindrome = st[label_l] + palindrome + st[label_r]
                    label_l -= 1
                    label_r += 1
                else:
                    palindromes.append(palindrome)
                    break
            palindromes.append(palindrome)
        return palindromes

    def extend_palindrome_even(st):
        palindromes = []
        for i in range(len(st)):
            label_l = i
            label_r = i + 1
            palindrome = ""
            while label_l >= 0 and label_r < len(st):
                if st[label_l] == st[label_r]:
                    palindrome = st[label_l] + palindrome + st[label_r]
                    label_l -= 1
                    label_r += 1
                else:
                    if palindrome not in palindromes:
                        palindromes.append(palindrome)
                    break
            if palindrome not in palindromes:
                palindromes.append(palindrome)
        return palindromes

    palin = extend_palindrome_odd(s) + extend_palindrome_even(s)
    length = 0
    palstr = ""
    for item in palin:
        if len(item) > length:
            length = len(item)
            palstr = item
    return palstr
print longestPalindrome("bb")
