class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        elif n == 0 or n == 1:
            return 1
        else:
            m = [0]*(n+1)
            m[0] = 1
            m[1] = 1
            for i in range(2,n+1):
                m[i] = m[i-1]+m[i-2]
            return m[n]

if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(10))
