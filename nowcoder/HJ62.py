class Solution:
    def solve(self, n):
        ans = 0
        while n != 0:
            if n & 1 == 1:
                ans += 1
            n >>= 1
        return ans


if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            print(Solution().solve(n))
        except:
            break
