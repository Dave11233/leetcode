from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:

        if not customers:
            return 0
        if X >= len(customers):
            return sum(customers)

        total = sum([customer for customer, gru in zip(customers, grumpy) if gru == 0])

        length = len(customers)

        max_increase = increase = sum([customer for customer, gru in zip(customers[:X], grumpy[:X]) if gru == 1])

        for i in range(X, length):
            increase += customers[i] * grumpy[i] - customers[i - X] * grumpy[i - X]
            max_increase = max(max_increase, increase)

        return total + max_increase


if __name__ == '__main__':
    print(Solution().maxSatisfied([4, 10, 10],
                                  [1, 1, 0],
                                  2)
          )
