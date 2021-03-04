class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_node = ListNode(0)
        pre = dummy_node
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                pre.next = l1
                pre = l1
                l1 = l1.next
            elif l1.val > l2.val:
                pre.next = l2
                pre = l2
                l2 = l2.next
            else:
                pre.next = l1
                pre = l1
                l1 = l1.next
                pre.next = l2
                pre = l2
                l2 = l2.next

        if l1 is None:
            pre.next = l2
        if l2 is None:
            pre.next = l1
        return dummy_node.next
