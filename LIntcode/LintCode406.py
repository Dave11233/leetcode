class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """

    def minimumSize(self, nums: list, s: int):
        if not nums:
            return -1
        if sum(nums) < s:
            return -1
        if sum(nums) == s:
            return len(nums)
        left, right = 0, 0
        total = 0
        ans = len(nums)
        while left < len(nums) and right < len(nums):
            total += nums[right]
            if total >= s:

                while total >= s and left <= right:
                    ans = min(ans, right - left + 1)
                    total -= nums[left]
                    left += 1
                right += 1
            else:
                right += 1
        return ans


if __name__ == '__main__':
    print(Solution().minimumSize([2,3,1,2,4,3], 7))
