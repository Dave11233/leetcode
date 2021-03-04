class Solution:

    def solve(self, s):
        if not s:
            return 0
        ans = 0
        for char in s:
            if ord("A") <= ord(char) <= ord("Z"):
                ans += 1
        return ans


if __name__ == '__main__':
    while True:
        try:
            s = input()
            print(Solution().solve(s))
        except EOFError:
            break