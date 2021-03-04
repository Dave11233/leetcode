class Solution:
    def solve(self, n):
        if n <= 0:
            return -1
        ans = [[0] * (2 * i + 1) for i in range(n)]
        for i in range(n):
            ans[i][2 * i] = 1
            ans[i][0] = 1

        for i in range(1, n):

            for j in range(1, 2 * i):
                start = j - 2 if j - 2 >= 0 else 0
                ans[i][j] = sum(ans[i - 1][start:j + 1])
        for index,j in enumerate(ans[-1]):
            if j % 2 == 0:
                return index + 1
        return -1


if __name__ == '__main__':
    while True:
        try:
            m = int(input())
            print(Solution().solve(m))
        except:
            break
