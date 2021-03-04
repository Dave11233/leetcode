class Solution:
    def solve(self, n):
        def helper(m):
            if m <= 2:
                return False
            ans = [1]
            for i in range(2, int(m ** 0.5) + 1):
                if m % i == 0:
                    ans.append(i)
                    ans.append(m // i)
            return sum(ans) == m

        return sum(list(map(helper, list(range(n + 1)))))


if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            print(Solution().solve(n))
        except:
            break
