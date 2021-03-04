class Solution:
    def oneCounter(self, n:int) -> int:
        ans = 0
        while n != 0:
            if n % 2 == 1:
                ans += 1
            n = n >> 1
        return ans


if __name__ == '__main__':
    m = int(input())
    print(Solution().oneCounter(10))
