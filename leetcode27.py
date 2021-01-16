class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        else:
            index = 0
            length = len(nums)
            for i in range(length):
                if nums[i] == val:
                    pass
                else:
                    nums[index] = nums[i]
                    index += 1
            nums = nums[:(index+1)]
            return index