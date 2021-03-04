class Solution:
    counter = 0

    def findTargetSumWays(self, nums, S: int) -> int:

        length = len(nums)

        def helper(nums, current_sum, start_index):

            if start_index == length:
                if current_sum == S:
                    self.counter += 1
                return

            helper(nums, current_sum + nums[start_index], start_index + 1)
            helper(nums, current_sum - nums[start_index], start_index + 1)

        helper(nums, 0, 0)

        return self.counter


if __name__ == '__main__':
    print(Solution().findTargetSumWays([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 0))
