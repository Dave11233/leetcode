class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        s_ = s.strip().split(" ")[-1]
        if s_ == " ":
            return 0

        return len(s_)
if __name__ == '__main__':
    solution =Solution()
    print(solution.lengthOfLastWord("a "))