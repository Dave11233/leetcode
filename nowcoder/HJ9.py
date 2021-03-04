class Solution:

    def getIrrepteadInteger(self, x):
        ans = 0
        visited = [False] * 10
        while x != 0:
            if not visited[x % 10]:
                ans = ans * 10 + x % 10
                visited[x % 10] = True
            x = x // 10
        return ans


if __name__ == '__main__':
    n = int(input())
    print(Solution().getIrrepteadInteger(n))
