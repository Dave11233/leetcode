
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        from collections import deque
        queue = deque([root])
        ret = []
        while queue:
            temp_queue = queue.copy()
            temp = []
            next_level = []
            flag = True
            pre = None
            while temp_queue:
                if flag:
                    pre = temp_queue.popleft()
                    flag = False
                    if pre.left is not None:
                        next_level.append(pre.left)
                    if pre.right is not None:
                        next_level.append(pre.right)
                    continue
                node = temp_queue.popleft()
                pre.next = node
                pre = node
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            ret.append(temp.copy())
            pre.next = None
            queue = deque(next_level)
        return root