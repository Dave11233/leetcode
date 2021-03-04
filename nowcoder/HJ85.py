class Solution:

    def solve(self, s):
        if not s:
            return 0
        ans = 0
        for i in range(len(s)):

            for j in range(len(s), i, -1):
                x = s[i:j]
                if x == x[::-1]:
                    ans = max(ans, j - i)
        return ans


if __name__ == '__main__':
    s = input()
    print(Solution().solve(s))