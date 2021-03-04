from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:

        if root is None:
            return []
        from collections import Counter
        ret = []

        def helper(node=root):
            if node is None:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            ret.append(left + right + node.val)
            return left + right + node.val

        helper()
        counter = Counter(ret)
        max_f = max(counter.values())

        return [key for key, value in counter.items() if value == max_f]