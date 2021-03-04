class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: given BST
    @param minimum: the lower limit
    @param maximum: the upper limit
    @return: the root of the new tree
    """

    def trimBST(self, root, minimum, maximum):
        if root is None:
            return None
        if root.val < minimum or root.val > maximum:
            return None
        else:
            new_root = TreeNode(root.val)
            new_root.left = self.trimBST(root.left, minimum, maximum)
            new_root.right = self.trimBST(root.right, minimum, maximum)

            return new_root
