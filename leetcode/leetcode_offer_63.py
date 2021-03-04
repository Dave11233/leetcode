class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0

        dp = [0 for _ in prices]

        for i in range(1,len(prices)):
            dp[i] = prices[i] - prices[0]

        for i in range(1,len(prices)):
            d = dp[i]
            for j in range(len(prices)-1,i,-1):
                d = max(d,dp[j]-dp[i])
            dp[i] = d
        print(dp)
        return max(dp)

if __name__ == '__main__':
    x = [7,1,5,3,6,4]
    solution = Solution()
    print(solution.maxProfit(x))