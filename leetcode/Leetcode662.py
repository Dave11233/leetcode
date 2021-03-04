

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:

        if root is None:
            return 0
        width = 0

        from collections import deque

        queue = deque([root, 1])

        while queue:
            width = max(width, queue[-1][-1] - queue[0][-1])
            temp_queue = queue.copy()
            next_level = []
            while temp_queue:
                node, i = temp_queue.popleft()
                if node.left is not None:
                    next_level.append([node.left, 2*i])
                if node.right is not None:
                    next_level.append([node.right, 2*i + 1])

            queue = deque(next_level)
        return width
