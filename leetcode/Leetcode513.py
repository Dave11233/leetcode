class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            raise ValueError("The root must not be None")
        from collections import deque
        queue = deque([root])
        ans = 0
        while queue:
            ans = queue[1].val
            temp_queue = queue.copy()
            temp = []
            next_level = []
            while temp_queue:
                node = temp_queue.popleft()
                temp.append(node.val)
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            queue = deque(next_level)
        return ans