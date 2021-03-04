from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        if not matrix:
            return []
        if len(matrix[0]) == 0:
            return [[]]
        ret = []
        m, n = len(matrix), len(matrix[0])
        for i in range(n):
            temp = []
            for j in range(m):
                x = matrix[j][i]
                temp.append(x)
            ret.append(temp.copy())
        return ret


if __name__ == '__main__':
    print(Solution().transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
