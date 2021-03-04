class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        if not nums:
            return True

        length = len(nums)
        cumsum = [0] * length
        cumsum[0] = nums[0]
        for i in range(1, len(nums)):
            cumsum[i] = cumsum[i - 1] + nums[i]
        for i in range(length - 1):
            for j in range(i + 1, length):
                total = nums[i] + cumsum[j] - cumsum[i]
                if total == k or (k != 0 and total % k == 0):
                    return True
        return False


if __name__ == '__main__':
    print(Solution().checkSubarraySum([23, 2, 6, 4, 7],
                                      0))
