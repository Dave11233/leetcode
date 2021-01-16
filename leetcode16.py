class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        assert nums
        assert len(nums) >= 3
        nums.sort()
        closestNum = nums[0] + nums[1] + nums[2]
        length = len(nums)
        for i in range(length - 2):
            l = i + 1
            r = length - 1
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]
                if abs(closestNum - target) > abs(threesum - target):
                    closestNum = threesum
                if threesum > target:
                    r -= 1
                elif threesum < target:
                    l += 1
                else:
                    return target
        return closestNum

if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSumClosest([1, 2, 4, 8, 16, 32, 64, 128], 82))
