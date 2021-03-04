class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    ans = 0

    def longestZigZag(self, root: TreeNode) -> int:
        def helper(path):
            if not path:
                return 0
            dp = [0] * len(path)
            dp[0] = 1
            for i in range(1, len(path)):
                if path[i] == path[i - 1]:
                    dp[i] = 1
                else:
                    dp[i] = dp[i - 1] + 1
            return max(dp)

        def dfs(r, path=[]):
            if r is None:
                # print(path)
                return
            if r.left is None and r.right is None:
                self.ans = max(self.ans, helper(path))
                return

            path.append(0)
            dfs(r.left, path)
            path.pop()

            path.append(1)
            dfs(r.right, path)
            path.pop()

        dfs(root, [])
        return self.ans
