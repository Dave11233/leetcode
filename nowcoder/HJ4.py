class Solution:
    def split(self, s):
        if not s:
            return ""
        length = len(s)
        ret = []
        for i in range(0, length, 8):
            temps = s[i:i + 8]
            if len(temps) == 8:
                ret.append(temps)
            else:
                ret.append(temps + "".join(["0"] * (8 - len(temps))))
        return ret


if __name__ == '__main__':
    while True:
        try:
            s = input()
            ans = Solution().split(s)
            for i in ans:
                print(i)
        except EOFError:
            break
