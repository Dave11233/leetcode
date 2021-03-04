class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.arr = []

        def helper(root):
            if root is None:
                return
            helper(root.left)
            self.arr.append(root.val)
            helper(root.right)

        helper(root)
        self.index = 0

    def next(self) -> int:
        val = self.arr[self.index]
        self.index += 1
        return val

    def hasNext(self) -> bool:
        return self.index < len(self.arr)
