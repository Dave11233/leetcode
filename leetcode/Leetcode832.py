from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        if not A:
            return []
        ret = []
        m, n = len(A), len(A[0])
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(0 if A[i][j] == 1 else 1)
            temp.reverse()
            ret.append(temp.copy())
        return ret