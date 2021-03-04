class Solution:
    def pivotIndex(self, nums: list) -> int:
        if not nums:
            return -1
        total = sum(nums)
        left = 0
        for i in range(len(nums)):
            right = total - left - nums[i]
            if left == right:
                return i
            left += nums[i]
        return -1


if __name__ == '__main__':
    print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))