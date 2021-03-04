class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        stack_l1 = []
        stack_l2 = []
        h1 = l1
        h2 = l2
        while h1 is not None or h2 is not None:
            if h1 is not None:
                stack_l1.append(h1)
                h1 = h1.next
            if h2 is not None:
                stack_l2.append(h2)
                h2 = h2.next
        if len(stack_l1) < len(stack_l2):
            stack_l1, stack_l2 = stack_l2, stack_l1
        h = ListNode(0)
        c = 0
        while stack_l1 and stack_l2:
            x1 = stack_l1.pop().val
            x2 = stack_l2.pop().val
            val = (x1 + x2 + c) % 10
            c = (x1 + x2 + c) // 10
            q = ListNode(val)
            q.next = h.next
            h.next = q
        while stack_l1:

            x1 = stack_l1.pop().val
            val = (x1 + c) % 10
            c = (x1 + c) // 10
            q = ListNode(val)
            q.next = h.next
            h.next = q
        if c >= 1:

            q = ListNode(c)
            q.next = h.next
            h.next = q
        return h.next


