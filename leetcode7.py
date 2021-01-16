class Solution:
    def reverse(self, x: int) -> int:

        sign = 1 if x >= 0 else -1
        y = str(y)
        y = y[::-1]
        y = int(y)
        y = y * sign
        if -(2**31) <= y <= (2**31 - 1):
            return y
        else:
            return 0
