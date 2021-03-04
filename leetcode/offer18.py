class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy_node = ListNode(0)
        dummy_node.next = head
        pre = dummy_node
        while head is not None:
            if head.val == val:
                pre.next = head.next
                break
            pre = head
            head = head.next

        return dummy_node.next