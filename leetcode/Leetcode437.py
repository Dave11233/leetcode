class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = 0

    def pathSum(self, root: TreeNode, sum: int) -> int:

        if not root:
            if sum == 0:
                return 1
            else:
                return 0

        def helper(node=root, prefix=[]):
            if not node:
                return
            if not prefix:
                prefix.append(node.val)
                if node.val == sum:
                    # nonlocal ans
                    self.ans += 1
            else:
                temp_sum = prefix[-1] + node.val

                for prefix_sum in prefix:
                    if temp_sum - prefix_sum == sum:
                        # nonlocal ans
                        self.ans += 1
                if temp_sum == sum:
                    self.ans += 1
                prefix.append(temp_sum)
            helper(node.left, prefix)
            helper(node.right, prefix)
            prefix.pop()

        helper()
        return self.ans
