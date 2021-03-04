class Solution:
    def solve(self, s:str):
        if not s:
            return 0
        if not s.startswith("0x"):
            raise ValueError("The string must start with 0x")
        temp_s = s[2:]
        # s.*
        ans = 0
        for i, char in enumerate(temp_s[::-1]):
            if char.isdigit():
                ans += (ord(char) - ord('0')) * (16 ** i)
            else:
                ans += (ord(char) - ord('A') + 10) * (16 ** i)
        return ans


if __name__ == '__main__':
    s = input()
    print(Solution().solve(s))