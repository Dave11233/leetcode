class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = []

        def helper(root, temp=[]):
            if not root:
                return
            if root.left is None and root.right is None:
                print(temp + [str(root.val)])
                res.append(temp.copy() + [root.val])
                return
            temp.append(str(root.val))
            helper(root.left, temp)
            helper(root.right, temp)
            temp.pop()

        helper(root)
        ans = sum([int("".join(i)) for i in res])
        return ans