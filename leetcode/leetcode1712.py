from typing import List


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0
        cumsum = [0] * (len(nums))
        cumsum[0] = nums[0]
        for i in range(1, len(nums)):
            cumsum[i] = nums[i] + cumsum[i - 1]
        ans = 0
        for i in range(1, len(nums)):
            left = cumsum[i - 1]
            for j in range(i, len(nums)):
                mid = cumsum[j] - left
                right = cumsum[-1] - mid - left
                if left <= mid <= right: ans += 1
        return ans
