# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        list_node = ListNode(0)
        list_node.next = head
        p = list_node.next
        pre = list_node
        while p is not None and p.next is not None:
            q = p.next
            temp = q.next
            q.next = p
            pre.next = q
            pre = p
            p.next = temp
            p = temp
        return list_node.next