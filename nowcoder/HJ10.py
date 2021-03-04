class Solution:
    def staticsTheChar(self, s: str) -> int:

        if not s:
            return 0
        ans = [0] * 128
        for char in s:
            if 0 <= ord(char) <= 127:
                ans[ord(char)] = 1
        return sum(ans)


if __name__ == '__main__':
    S = input()
    print(Solution().staticsTheChar(S))
