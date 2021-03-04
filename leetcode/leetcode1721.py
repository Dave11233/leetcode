class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        p = head
        while k > 1 and p is not None:
            p = p.next
            k -= 1
        if p is None:
            return head
        temp_p = p
        # print(temp_p.val)
        q = head
        while p.next is not None:
            p = p.next
            q = q.next
        print(temp_p.val, q.val)
        temp_p.val, q.val = q.val, temp_p.val
        return head
