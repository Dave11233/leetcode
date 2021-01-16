class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        length = len(nums)
        left = 0
        right = length - 1
        nums.sort()
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                return [nums[left], nums[right]]
        return []
