class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        ans = []

        def dfs(r, res=[]):
            if r is None:
                ans.append("->".join(res.copy()))
            res.append(str(r.val))
            dfs(r.left)
            dfs(r.right)
            res.pop()
        dfs(root)
        return ans
