class Solution:
    def lengthOfLIS(self, nums) -> int:
        length = len(nums)
        dp = [[0] * length for _ in range(length)]
        dp[0][0] = 1
        max_len = -1
        # for i in range(length):
        #     dp[0][i] = 1 if nums[i] >= nums[0] else 0
        for i in range(length):
            dp[i][i] = 1
        for i in range(1, length):
            for j in range(1, i):
                if nums[j] > nums[i]:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + 1
                max_len = max(max_len, dp[i][j])
        return max_len


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
