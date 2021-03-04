class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (num1 < num2)
    """

    def twoSum7(self, nums: list, target: int):

        if not nums or len(nums) < 2:
            return []
        # nums.sort(reverse=target >= 0)
        cache = {}
        if target >= 0:
            for i in range(len(nums)):
                if nums[i] - target not in cache:
                    cache[nums[i]] = True
                else:
                    return [nums[i] - target, nums[i]]
        else:
            for i in range(len(nums)):
                if nums[i] + target not in cache:
                    cache[nums[i]] = True
                else:
                    return [nums[i] + target, nums[i]]

        return []
