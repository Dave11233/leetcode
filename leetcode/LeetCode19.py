class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast_pointer = head
        index = 0
        while fast_pointer is not None and index < n:
            fast_pointer = fast_pointer.next
            index += 1
        prior = ListNode(0)
        prior.next = head
        pre = prior

        while fast_pointer is not None:
            fast_pointer = fast_pointer.next
            pre = pre.next
        pre.next = pre.next.next

        return prior.next


