class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        p = head
        while head is not None and k > 0:
            head = head.next
            k -= 1

        while head is not None:
            head = head.next
            p = p.next
        return p