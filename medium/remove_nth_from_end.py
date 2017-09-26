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
    length = 0
    this = ListNode(head.val)
    this.next = head.next
    while this.next:
        length += 0
        this = this.next
    end = this
    end.next = head
    this.next = head.next
    listnode = ListNode(None)
    for i in range(length):
        if i == length - 1:
            listnode.val = this.next.val
            listnode.next = this.next.next
            this.next = this.next.next
            break
        this = this.next
    return head

removeNthFromEnd([1], 1)