class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None
        fast = head.next.next
        slow = head
        while fast != slow and fast is not None:
            slow = slow.next
            if fast.next is None:
                return None
            fast = fast.next.next
        if fast is None :
            return None
        while True:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return slow

        return None