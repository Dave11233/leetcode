# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:

        if not root:
            return []
        from collections import deque
        ans = []
        queue = deque([root])
        while queue:
            temp_deque = queue.copy()
            new_deque = deque([])
            ans.append(
                max(temp_deque, key=lambda x: x.val).val
            )
            while temp_deque:
                new_root = temp_deque.popleft()
                if new_root.left is not None:
                    new_deque.append(new_root.left)
                if new_root.right is not None:
                    new_deque.append(new_root.right)
            queue = new_deque.copy()
        return ans
