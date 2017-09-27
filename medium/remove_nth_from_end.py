# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    ret = ListNode(0)
    ret.next = head
    first = second = ret
    for i in range(n + 1):
        first = first.next
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next

    return ret.next
