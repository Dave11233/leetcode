class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root: TreeNode):

        def helper(tree_node, min_value, max_value):
            if tree_node is None:
                return True
            if tree_node.val >= max_value or tree_node.val <= min_value:
                return False
            left = helper(tree_node.left, min_value, tree_node.val)
            right = helper(tree_node.right, tree_node.val, max_value)
            return left and right

        return helper(root, -float("inf"), float("inf"))
