def reverse_words(s):
    return " ".join(map(lambda r: r[::-1], s.split(' ')))

print reverse_words("Let's take LeetCode contest")
