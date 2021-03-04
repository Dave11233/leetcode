class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    ans = None

    def inorderSuccessor(self, root, p):
        if p is None or root is None:
            return None
        if p.right is not None:
            return p.right
        flag = False
        def helper(root, p):
            if root is None:
                return

            helper(root.left, p)
            if root.val > p.val:
                nonlocal flag
                if not flag:
                    self.ans = root
                    flag = True
            helper(root.right, p)

        helper(root, p)
        return self.ans
