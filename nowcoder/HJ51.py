class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def build(self, node_list):
        if not node_list:
            return None
        head = self.__class__(val=node_list[0], next=None)
        p = head
        for i in node_list[1:]:
            q = self.__class__(i)
            p.next = q
            p = q
        return head

class Solution:
    def solve(self, head, k):
        data = []
        while head:
            data.append(head.val)
            head = head.next
        return data[-k]

if __name__ == '__main__':
    while True:
        try:
            s = input()
            k = int(input())
            node_list = s.split()
            node = Node()
            head = node.build(node_list)
            print(Solution().solve(head, k))
        except EOFError:
            break

