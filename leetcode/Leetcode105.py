from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        value = preorder[0]
        root = TreeNode(value)
        index = inorder.index(value)
        left_inorder = inorder[:index]
        right_inorder = inorder[(index + 1):]
        root.left = self.buildTree(preorder[1:index+1], left_inorder)
        root.right = self.buildTree(preorder[index + 1:], right_inorder)
        return root
