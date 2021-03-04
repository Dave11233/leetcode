class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        if root is None or k < 0:
            raise ValueError("the root of the tree is not None or the k must be beyond 0")

        array = []

        def helper(root):
            if root is None:
                return
            helper(root.left)
            array.append(root.val)
            helper(root.right)

        helper(root)
        if k > len(array):
            raise RuntimeError("The k is beyond the length of the binary tree")
        return array[k - 1]
