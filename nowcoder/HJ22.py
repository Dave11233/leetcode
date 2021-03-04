class Solution:

    def solve(self, n: int) -> int:
        if n < 3:
            return 0
        ans = 0
        while n >= 3:
            ans += n // 3
            n = n // 3 + n % 3
        if n == 2:
            ans += 1
        return ans


if __name__ == '__main__':
    while True:
        try:
            m = int(input())
            print(Solution().solve(m))
        except:
            break
