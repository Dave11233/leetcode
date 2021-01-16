class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums) + 1
        for i in range(0, length):
            if i ^ nums[i] != 0:
                return i
        return -1