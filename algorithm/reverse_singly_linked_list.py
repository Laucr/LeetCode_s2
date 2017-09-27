class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_link(list_head):
    """
    :type list_head: ListNode
    :rtype: ListNode
    """
    prevp = None
    headp = list_head

    while headp:
        nextp = headp.next
        headp.next = prevp
        prevp = headp
        headp = nextp

    return prevp

l = []
for i in range(5):
    l.append(ListNode(i))

for i in range(4):
    l[i].next = l[i + 1]
l[-1].next = None

i = reverse_link(l[0])

print i.val
while i.next:
    print i.next.val
    i = i.next
