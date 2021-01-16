class Solution:
    def findDuplicate(self, nums):
        def helper(nums_list):
            if len(nums_list) < 2:
                return nums_list
            else:
                pivot = nums_list[0]
                less_than_pivot = [x for x in nums_list[1:] if x <= pivot]
                more_than_pivot = [x for x in nums_list[1:] if x > pivot]
                return helper(less_than_pivot) + [pivot] + helper(more_than_pivot)

        return helper(nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findDuplicate([1, 3, 4, 2, 2]))
