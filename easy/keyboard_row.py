# ugly


def in_which_row(s):
    pointer = s.lower()[0]
    if pointer in row[0]:
        return 0
    elif pointer in row[1]:
        return 1
    else:
        return 2


def not_one_row(s, r):
    for i in s.lower():
        if i not in row[r]:
            return True
    return False


def find_words(w):
    delword = []
    for i in range(len(w)):
        r = in_which_row(w[i])
        if not_one_row(w[i], r):
            delword.append(w[i])
    return [word for word in w if word not in delword]

row = (
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm"
)

words = ["Aasdfghjkl","Qwertyuiop","zZxcvbnm"]

print find_words(words)
