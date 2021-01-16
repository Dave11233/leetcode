class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        head_ = ListNode(0)
        head_.next = head
        pre = head_
        while head is not None:
            next = head.next
            flag = False
            while next is not None and next.val == head.val:
                flag = True
                next = next.next
            if flag:
                head = next
                pre.next = head
            else:
                pre = head
                head = head.next
        return head_.next

