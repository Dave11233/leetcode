class Solution:
    def hammingWeight(self, n: int) -> int:
        # count = 0
        # while n:
        #     x = n % 2
        #     n //= 2
        #     if x == 1:
        #         count += 1
        # return count
        count = 0
        while n:
            x = n % 2
            n <<= 2
            if x:
                count += 1
        return count
