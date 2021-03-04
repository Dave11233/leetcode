class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(root, left_boundary, right_boundary):
            if root is None:
                return True
            if root.val > left_boundary or root.val < right_boundary:
                return False
            left = helper(root.left, left_boundary, root.val)
            right = helper(root.right, root.val, right_boundary)
            return left and right

        return helper(root, -float("inf"), float("inf"))
