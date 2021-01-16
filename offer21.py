class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        for num in nums:
            if num & 1 == 0:
                left.append(num)
            else:
                right.append(num)
        return left + right