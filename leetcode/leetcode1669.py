class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        p = list1
        q = list1
        while a >= 1 or b >= 0:
            if a >= 1:
                p = p.next
                a -= 1
            if b >= 0:
                q = q.next
                b -= 1
        if list2 is None:
            p.next = q
            return list1
        p.next = list2
        p = list2
        while p.next is not None:
            p = p.next
        p.next = q
        return list1
