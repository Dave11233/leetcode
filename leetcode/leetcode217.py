class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        def helper(nums):
            if not nums:
                return False
            if nums[0] in nums[1:]:
                return True
            left = [i for i in nums[1:] if i <= nums[0]]
            right = [i for i in nums[1:] if i > nums[0]]
            left_flag = helper(left)
            right_flag = helper(right)
            return left_flag or right_flag
        return helper(nums)