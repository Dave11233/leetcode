class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp1 = [0] * (len(nums))
        dp1[0] = 0
        dp1[1] = nums[1]
        for i in range(2, len(nums)):
            dp1[i] = max(dp1[i - 2] + nums[i], dp1[i - 1])
        dp2 = [0] * len(nums)
        dp2[0], dp2[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            # dp2[i] = max(dp2[i - 2] + nums[i], dp2[i - 1])
            dp2[i] = max(dp2[i - 1], nums[i] + dp2[i - 2])
        return max(dp1[-1], dp2[-2])

        # n = len(nums)
        # if n == 0:
        #     return 0
        # if n <= 2:
        #     return max(nums)
        # # 不抢第一个
        # dp1 = [0] * n
        # dp1[0] = 0
        # dp1[1] = nums[1]
        # for i in range(2, n):
        #     dp1[i] = max(dp1[i - 1], nums[i] + dp1[i - 2])
        #
        # # 不抢最后一个
        # dp2 = [0] * n
        # dp2[0] = nums[0]
        # dp2[1] = max(nums[0], nums[1])
        # for i in range(2, n - 1):
        #     dp2[i] = max(dp2[i - 1], nums[i] + dp2[i - 2])
        # return max(dp1[- 1], dp2[- 2])



if __name__ == '__main__':
    print(Solution().rob(
        [1, 2, 3, 1]
    ))
