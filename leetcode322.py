class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                dp[i] = min(dp[i], dp[i - coin] + 1 if i - coin >= 0 else float("inf"))
        return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == '__main__':
    print(Solution().coinChange(
        coins=[1, 2, 5], amount=11
    ))
