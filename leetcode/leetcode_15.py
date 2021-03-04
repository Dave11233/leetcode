class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_set = list(set(nums))
        nums_set.sort()
        length = len(nums_set)
        for i in range(1,length-1):
            left = i - 1
            right = i + 1
