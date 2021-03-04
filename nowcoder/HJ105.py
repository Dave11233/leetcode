from typing import List
from typing import Tuple


class Solution:

    def solve(self, data: List[int]) -> Tuple[float, int]:
        if not data:
            return 0.0, 0
        # 统计其中的负数个数并求所有非负数的平均值
        beyond_zero = [i for i in data if i >= 0]

        average = sum(beyond_zero) / len(beyond_zero) if len(beyond_zero) != 0 else 0.0
        counter = len(data) - len(beyond_zero)
        return average, counter


if __name__ == '__main__':
    data = []
    while True:
        try:
            data.append(int(input()))
        except:
            break
    average, counter = Solution().solve(data)
    print(counter)
    print(average)
