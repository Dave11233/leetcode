class Solution:
    def threeSum(self, nums: list):
        assert len(nums) >= 3
        nums.sort()
        res = set()
        length = len(nums) - 1
        for i in range(1, len(nums) - 1):
            left = i - 1
            right = i + 1
            while left >= 0 and right <= length:
                target = nums[left] + nums[i] + nums[right]
                if target > 0:
                    left -= 1
                elif target < 0:
                    right += 1
                else:
                    if (nums[left], nums[i], nums[right]) not in res:
                        res.add((nums[left], nums[i], nums[right]))
                    left -= 1
        return list(res)


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
