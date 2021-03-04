class Solution:

    def solve(self, s: str):
        if not s:
            return 0
        temp_s = s.split(" ")[-1]
        return len(temp_s)


if __name__ == '__main__':
    # print(Solution().solve('XSUWHQ'))

    s = input()
    print(Solution().solve(s))