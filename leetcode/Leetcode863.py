# from typing import List
#
#
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#
# class Solution:
#     def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
#         if not root:
#             return []
#         from collections import deque
#         queue = deque([root])
#         ret = []
#         temp_nodes = []
#         while queue:
#             temp_queue = queue.copy()
#             next_level = []
#             while temp_queue:
#                 node = temp_queue.popleft()
#                 if node.val == target:
#                     temp_nodes.append(node)
#                 if node.left is not None:
#                     next_level.append(node.left)
#                 if node.right is not None:
#                     next_level.append(node.right)
#             queue = deque(next_level)
#         while temp_nodes:
#             node = temp_nodes.pop(0)