from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        from sortedcontainers import SortedList
        sorted_apple = SortedList()
        res_days = 0
        passed_days = 0
        while sorted_apple or passed_days < len(days):
            # 判断是否有过期苹果
            while sorted_apple and sorted_apple[0][0] <= passed_days:
                sorted_apple.pop(0)

            # 添加新鲜苹果
            if passed_days < len(days) and apples[passed_days]:
                sorted_apple.add([passed_days + days[passed_days], apples[passed_days]])

            # 吃苹果
            if sorted_apple:
                if sorted_apple[0][1] > 1:
                    sorted_apple[0][1] -= 1
                else:
                    sorted_apple.pop(0)
                res_days += 1
            passed_days += 1
        return res_days