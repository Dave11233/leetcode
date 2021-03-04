class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(n):
            if n == 0:
                return 1
            if n == 1:
                return x
            y = helper(n // 2)
            return y ** 2 if n & 1 == 0 else x * y ** 2

        return helper(n) if n >= 0 else 1.0/helper(-n)


if __name__ == '__main__':
    print(Solution().myPow(0.00001, 2147483647))
