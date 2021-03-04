# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        if root is None:
            return []
        res = []
        path = [root.vale]

        def helper(tree_node):
            if tree_node is None:
                res.pop()
                return
            path.append(tree_node.val)
            if tree_node.left is None and tree_node.right is None:
                if sum(path) == sum:
                    res.append(path.copy())
                return
            helper(tree_node.left)
            helper(tree_node.right)

        helper(root.left)
        helper(root.right)
        return res
