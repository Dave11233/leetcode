class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 2:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(n + 1):
            for j in range( i):
                dp[i] = max(dp[i], dp[j] * (i - j))
        return dp[-1]


if __name__ == '__main__':
    print(Solution().integerBreak(10))
