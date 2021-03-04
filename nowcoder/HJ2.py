from collections import Counter


class Solution:
    def solve(self, s:str, char:str):
        if not s:
            return 0
        if char.isupper():
            return s.upper().count(char)
        else:
            return s.lower().count(char)


if __name__ == '__main__':
    s = input()
    char = input()
    print(Solution().solve(s, char))