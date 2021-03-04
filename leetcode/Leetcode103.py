from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        level = 0
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
                node = temp_queue.pop()
                temp.append(node.val)
                if level & 1 == 0:
                    if node.left is not None:
                        next_level.append(node.left)
                    if node.right is not None:
                        next_level.append(node.right)
                else:
                    if node.right is not None:
                        next_level.append(node.right)
                    if node.left is not None:
                        next_level.append(node.left)
            ret.append(temp.copy())
            queue = deque(next_level)
            level += 1
        return ret