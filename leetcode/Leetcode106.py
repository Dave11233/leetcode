from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        value = postorder[-1]
        root = TreeNode(value)
        index = inorder.index(value)
        left_inorder = inorder[:index]
        right_inorder = inorder[(index + 1):]
        root.left = self.buildTree(left_inorder, postorder[:index])
        root.right = self.buildTree(right_inorder, postorder[index: -1])
        return root