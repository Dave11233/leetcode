class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        length = len(a)
        res = []
        for i in range(length + 1):
            tmp = a.copy()
            tmp[i] = 1
            total = 1
            for j in tmp:
                total *= j
            res.append(total)
        return res