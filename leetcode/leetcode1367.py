class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        from collections import deque
        if head is None:
            return True
        if root is None:
            return False
        d = deque(root)

        def helper(r, h):
            if h is None:
                return True
            if r is None:
                return False

            if r.val == h.val:
                left = helper(h.next, r.left)
                right = helper(h.next, r.right)
                return left or right
            else:
                return False

        while len(d) != 0:
            q = d.popleft()
            if q.val == head.val:
                if helper(q, head):
                    return True
            if q.left is not None:
                d.append(q.left)
            if q.right is not None:
                d.append(q.right)
        return False
