# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        head = ListNode(0)
        temp_head = head
        while p1 is not None and p2 is not None:
            if p1.val == p2.val:
                q1 = p1.next
                q2 = p2.next
                temp_head.next = p1
                temp_head = p1
                temp_head.next = p2
                temp_head = p2
                p1 = q1
                p2 = q2
            elif p1.val < p2.val:
                q1 = p1.next
                temp_head.next = p1
                temp_head = p1
                p1 = q1
            else:
                q2 = p2.next
                temp_head.next = p2
                temp_head = p2
                p2 = q2
        if p1 is not None:
            temp_head.next = p1
        if p2 is not None:
            temp_head.next = p2
        return head.next

