class Solution:
    def solve(self, s:str):

        if not s:
            return "", "0"
        ans_str = ""
        ans_length = 0
        i = 0
        j = 0
        length = len(s)
        while i < length and j < length:
            if s[i].isdigit():
                j = i + 1
                while not s[j].isdigit():
                    j += 1
                if len(s[i:j]) > len(ans_str):
                    ans_str = s[i:j]
                    ans_length = len(ans_str)
                i = j

            else:
                i += 1
        return ans_str, str(ans_length)



if __name__ == '__main__':
    while True:
        try:
            S = input()
            ans = Solution().solve(S)
            print(",".join(ans))
        except EOFError:
            break
