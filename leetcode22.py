class Solution:
    def generateParenthesis(self, n: int):
        def helper(string, left, right):
            if left > n :
                return
            if right > left:
                return
            if right == n:
                print(string)
                return
            if right <= left:
                helper(string + "(", left + 1, right)
                helper(string + ")", left, right + 1)
        helper("", 0, 0)


if __name__ == '__main__':
    solution = Solution()
    solution.generateParenthesis(3)
