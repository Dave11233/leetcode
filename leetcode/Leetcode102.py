from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        queue = deque([root])
        ret = []
        while queue:
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
            ret.append(temp.copy())
            queue = deque(next_level)
        return ret