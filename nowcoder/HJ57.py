class Solution:
    def high_accuracy_add(self, s1: str, s2: str):
        if not s1 and not s2:
            return "0"
        if not s1:
            return s2
        if not s2:
            return s1
        if not s1.isdigit() or not s2.isdigit():
            return ""
        x1 = s1 if len(s1) >= len(s2) else s2
        x2 = s1 if len(s1) < len(s2) else s2
        print(len(x1), len(x2))
        x1 = x1[::-1]
        x2 = x2[::-1]
        c = 0
        min_length = len(x2)
        ans = ""
        for i in range(min_length):
            ans += str((int(x1[i]) + int(x2[i]) + c) % 10)
            c = (int(x1[i]) + int(x2[i]) + c) // 10

        for j in range(min_length, len(x1)):
            ans += str((int(x1[j]) + c) % 10)
            c = (int(x1[j]) + c) // 10

        if c > 0:
            ans += "1"
        return ans[::-1]


if __name__ == '__main__':
    while True:
        try:
            s1 = input()
            s2 = input()
            print(Solution().high_accuracy_add(s1, s2))
        except EOFError:
            break
