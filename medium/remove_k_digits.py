def removeKdigits(num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """

    st = []
    for d in num:
        while k and st and st[-1] > d:
            st.pop()
            k -= 1
        st.append(d)
    return ''.join(st[:-k or None]).lstrip('0') or '0'

print removeKdigits("0", 3)
