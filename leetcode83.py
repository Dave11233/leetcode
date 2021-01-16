class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        head_ = head
        while head_ is not None:
            next = head_.next

            while next is not None and next.val == head_.val:
                flag = True
                next = next.next
            head_.next = next
        return head
