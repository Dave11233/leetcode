class Solution:
    def firstUniqChar(self, s: str) -> str:
        length = len(s)
        from collections import Counter
        couter = Counter(s)
        x = s.lower()
        for i in range(length):
            char = x[i]
            if couter[char] == 1:
                return char
        return " "

if __name__ == '__main__':
    s = "cC"
    solution = Solution()
    print(solution.firstUniqChar(s))