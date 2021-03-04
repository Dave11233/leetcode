class Solution:

    def solve(self, s1:str, s2:str):
        if not s1 or not s2:
            return 0
        m, n = len(s1), len(s2)
        dp = [[0] * (n+1) for _ in range(m + 1)]
        ans = 0
        for i in range(1, m+1):

            for j in range(1, n+1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + 1
                    ans = max(ans, dp[i][j])
        return ans


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    print(Solution().solve(s1, s2))