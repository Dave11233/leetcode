class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sortColors(self, nums):
        if not nums:
            return []
        from collections import Counter
        res = []
        counter = Counter(nums)
        for i in range(3):
            if i in counter:
                res += [i]*counter[i]
        return res