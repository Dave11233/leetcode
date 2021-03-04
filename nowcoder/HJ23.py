from collections import Counter


class Solution:
    def solve(self, s: str):
        if not s:
            return ""

        counter = Counter(s)
        min_value = min(zip(counter.keys(), counter.values()), key=lambda x: x[1])[1]
        ans = ""
        for i in s:
            if counter[i] != min_value:
                ans += i
        return ans


if __name__ == '__main__':
    while True:
        try:
            s = input()
            print(Solution().solve(s))
        except:
            break