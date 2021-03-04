from typing import List


class Solution:
    def solve(self, steps: List[int]) -> int:
        if not steps:
            return 0
        dp = [1] * len(steps)
        ans = 0
        for i in range(len(steps)):
            for j in range(i):
                if steps[i] > steps[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(dp[i], ans)
        return ans


if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            steps = list(map(int, input().split()))
            print(Solution().solve(steps))
        except EOFError:
            break
