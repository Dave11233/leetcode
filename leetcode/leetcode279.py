class Solution:
    def numSquares(self, n: int) -> int:
        import math
        if int(math.sqrt(n)) ** 2 == n:
            return 1
        dp = [float("inf")] * (n + 1)
        j = 1
        while j * j <= n:
            dp[j * j] = 1
            j += 1
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[-1]


if __name__ == '__main__':
    print(Solution().numSquares(6366))
