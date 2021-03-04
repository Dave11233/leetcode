class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """

    def searchRange(self, root, k1, k2):

        ans = []

        def inordervisit(root):
            if root is None:
                return
            inordervisit(root.left)
            if k1 <= root.val <= k2:
                ans.append(root.val)
            inordervisit(root.right)

        inordervisit(root)
        return ans
