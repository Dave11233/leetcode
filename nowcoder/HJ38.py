from typing import Tuple

class Solution:

    def solve(self, length: float) -> Tuple[float, float]:
        ans = 0.0
        first_length = length
        for i in range(5):
            ans += length
            length = length / 2
        return ans * 2 - first_length, length


if __name__ == '__main__':
    n = float(input())
    ans, length = Solution().solve(n)
    print("%.6f" % ans)
    print("%.6f" % length)
