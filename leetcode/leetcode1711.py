class Solution:
    def countPairs(self, deliciousness) -> int:
        from collections import defaultdict
        answer = 0
        mod = 1000000007
        freq_map = defaultdict(int)
        for x in deliciousness:
            for k in range(22): answer += freq_map[2 ** k - x]
            freq_map[x] += 1
        return answer % mod


if __name__ == '__main__':
    print(Solution().countPairs(
        [149, 107, 1, 63, 0, 1, 6867, 1325, 5611, 2581, 39, 89, 46, 18, 12, 20, 22, 234]
    )
    )
