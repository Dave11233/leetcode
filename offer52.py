class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        from collections import deque
        head_a_deque = deque()
        head_b_deque = deque()
        while headA is not None:
            head_a_deque.append(headA)
            headA = headA.next
        while headB is not None:
            head_b_deque.append(headB)
            headB = headB.next
        while len(head_b_deque) != 0 and len(head_a_deque) != 0:
            head_a = head_a_deque.pop()
            head_b = head_b_deque.pop()
            if head_a != head_b:
                return head_a.next
        return None
        