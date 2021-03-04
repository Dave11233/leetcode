from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def nextLargerNodes(self, arr):
        if not arr:
            return []
        ans = [0] * len(arr)
        stack = []
        for i, num in enumerate(arr):

            if len(stack) == 0:
                stack.append([num, i])
            else:
                if stack[-1][0] < num:
                    while len(stack) != 0 and stack[-1][0] < num:
                        _, index = stack.pop()
                        ans[index] = num
                stack.append([num, i])

        return ans


if __name__ == '__main__':
    print(Solution().nextLargerNodes([1, 7, 5, 1, 9, 2, 5, 1]))
