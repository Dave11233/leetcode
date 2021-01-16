class Solution:
    def removeDuplicates(self, nums) -> int:
        length = len(nums)
        index = 0
        for i in range(1, length):
            if nums[index] != nums[i]:
                index += 1
                nums[index] = nums[i]
        print(nums[:(index+1)])
        return index+1


if __name__ == '__main__':
    x = [0,0,1,1,1,2,2,3,3,4]
    solution = Solution()
    print(solution.removeDuplicates(x))