class Solution:
    def permuteUnique(self, nums):
        res = []

        def helper(list_nums=nums, temp_ans=[]):
            if len(list_nums) == 1:
                # temp_ans += list_nums
                res.append(temp_ans + list_nums)
                return
            if len(temp_ans) > len(nums):
                return
            list_nums.sort()

            for i in range(len(list_nums)):
                if i > 0 and list_nums[i] == list_nums[i - 1]:
                    continue
                else:
                    temp_ans.append(list_nums[i])
                    helper(list_nums[:i] + list_nums[i + 1:], temp_ans)
                    temp_ans.pop()
        helper()
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.permuteUnique([1, 1, 2]))
