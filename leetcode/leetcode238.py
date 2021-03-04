class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from collections import deque
        a = [1]
        b = deque([1])
        multiply = 1
        for i in nums[:-1]:
            multiply *= i
            a.append(multiply)
        multiply = 1
        for i in range(len(nums), 0, -1):
            multiply *= nums[i]
            b.appendleft(multiply)
        res = []
        for x,y in zip(a,b):
            res.append(x*y)
        return res
