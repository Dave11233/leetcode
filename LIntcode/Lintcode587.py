class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """

    def twoSum6(self, nums: list, target: int):
        if not nums:
            return 0
        if len(nums) <= 1:
            return 0
        nums.sort()
        left, right = 0, len(nums) - 1
        ans = 0
        while left < right:
            if nums[left] + nums[right] == target:
                ans += 1
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return ans


if __name__ == '__main__':
    print(
        Solution().twoSum6([1, 1, 2, 45, 46, 46], 47)
    )
