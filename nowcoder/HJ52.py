class Solution:

    def solve(self, s1: str, s2: str):
        m = len(s1)
        n = len(s2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for i in range(n + 1):
            dp[0][i] = i
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s[j - 1]:
                    cost = 0
                else:
                    cost = 1
                dp[j][i] = max(dp[j - 1][i - 1] + cost, dp[j - 1][i] + 1, dp[j][i - 1] + 1)

        return dp[-1][-1]


if __name__ == '__main__':

    while True:
        try:
            S1 = input()
            S2 = input()
            print(Solution().solve(S1, S2))
        except EOFError:
            break
