import collections


def leastInterval(tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    d = collections.Counter(tasks)
    counts = d.values()
    longest = max(counts)
    ans = (longest - 1) * (n + 1)
    for count in counts:
        ans += count == longest and 1 or 0
    return max(len(tasks), ans)


print leastInterval(["A", "A", "A", "A", "B", "B", 'B', 'C', 'C', 'C', 'D', 'D', 'D'], 2)
