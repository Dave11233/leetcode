class Solution:
    def numDecodings(self, s: str) -> int:
        if s.startswith("0"):
            return 0
        if len(s) == 1:
            return 1
        dp = [0] * len(s)
        dp[0] = 1
        if int(s[0]) > 2 and s[1] == "0":
            return 0
        if 11 <= int(s[:2]) <= 26:
            if int(s[:2]) == 20:
                dp[1] = 1
            else:
                dp[1] = 2
        else:
            dp[1] = 1
        for i in range(2, len(s)):
            if s[i] == '0' and s[i - 1] == '0':
                return 0
            elif s[i] == "0":
                if int(s[i - 1]) > 2:
                    return 0
                dp[i] = dp[i - 2]
            elif 11 <= int(s[i - 1:i + 1]) <= 26 and s[i] != "0":
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        # print(dp)
        return dp[-1]


if __name__ == '__main__':
    print(Solution().numDecodings("30"))
