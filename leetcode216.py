class Solution:
    def combinationSum3(self, k: int, n: int):
        res = []

        def helper(index=1, temp=[]):
            if sum(temp) > n:
                return
            if len(temp) > k:
                return
            if len(temp) == k:
                if sum(temp) == n:
                    res.append(temp.copy())
                return
            for i in range(index, 10):
                if i not in temp:
                    temp.append(i)
                    helper(i + 1, temp)
                    temp.pop()

        helper()
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum3(3, 7))
