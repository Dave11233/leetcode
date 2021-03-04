class TreeNode:
    def __init__(self, val):
        self.val = val


class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """

    def kthSmallest(self, root, k):

        ans = 0
        counter = 0

        def helper(root):
            if root is None:
                return
            helper(root.left)
            nonlocal counter
            counter += 1
            if counter == k:
                nonlocal ans
                ans = root.val
            helper(root.right)

        helper(root)
        return ans
