class Solution:
    def maxProduct(self, nums) -> int:
        if not nums:
            return 0
        max_value = -float("inf")
        imax , imin = 1, 1
        for num in nums:
            if num < 0:
                imax, imin = imin, imax
            imax = max(imax * num, num)
            imin = min(imin * num, num)
            max_value = max(imax, max_value)
        return max_value