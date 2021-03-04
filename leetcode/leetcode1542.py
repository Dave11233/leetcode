from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        temp_ans = [[]]
        ans = set()

        from collections import Counter
        counter = Counter(arr)
        for i, values in counter.items():
            temp_ans_copy = temp_ans.copy()
            for j in temp_ans:
                for k in range(values):
                    if sum(j + [i] * (k + 1)) & 1 == 1:
                        ans.add(sum(j + [i] * (k + 1)))
                    temp_ans_copy.append(j + [i] * (k + 1))
            temp_ans = temp_ans_copy.copy()
        print(temp_ans)
        x = set([sum(item) for item in temp_ans if sum(item) & 1 == 1])
        return len(ans), len(x), len(temp_ans)


if __name__ == '__main__':
    print(Solution().numOfSubarrays([1, 2, 3, 4, 5, 6, 7]))
