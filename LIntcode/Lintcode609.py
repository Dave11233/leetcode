class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums:list, target:int):
        if not nums or len(nums) < 2:
            return 0
        nums.sort()
        left = 0
        ans = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                ans += right - left
                left += 1
        return ans