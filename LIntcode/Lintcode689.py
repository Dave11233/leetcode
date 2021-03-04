class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):


        ans = []
        cache = set()
        def visit(root):
            if root is None:
                return
            visit(root.left)
            if n - root.val not in cache:
                cache.add(root.val)
            else:
                nonlocal ans
                ans = [n - root.val, root.val]

            visit(root.right)

        visit(root)
        return ans