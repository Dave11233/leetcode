class Solution:
    def myPow(self, x: float, n: int) -> float:

        # res = 1
        m = n if n >= 0 else -n
        t = x if n >= 0 else 1/x
        def helper(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            else:
                left = helper(x, n // 2)
                right = helper(x, n - n // 2)
                return left * right
        return helper(t, m)

        # while m != 0:
        #     if m & 1 == 1:
        #         res *= t
        #
        #     t *= t
        #     m >>= 1
        # return res

if __name__ == '__main__':
    x = 2
    y = 10
    solution = Solution()
    print(solution.myPow(x, y))
