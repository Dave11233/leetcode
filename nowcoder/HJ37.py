class Solution:

    def solve(self, n):
        if n <= 2:
            return 1
        ans = [1, 0, 0]
        for i in range(n + 1):
            if i > 4:
                ans[0] += ans[2]
            if i > 3:
                ans[2] = ans[1]
            if i > 2:
                ans[1] = ans[0]

        return sum(ans)


if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            print(Solution().solve(n))
        except:
            pass
