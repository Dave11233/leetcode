class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(temp):
            if len(temp) == len(nums):
                res.append(temp.copy())
                return
            for i in nums:
                if i not in temp:
                    temp.append(i)
                    helper(temp)
                    temp.pop()
        helper([])
        return res