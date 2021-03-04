class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()
        i, j = 0, 0
        abs_min = float("inf")
        while i < len(a) and j < len(b):
            abs_min = min(abs_min, abs(a[i] - b[j]))
            if a[i] < b[j]:
                i += 1
            elif a[i] > b[j]:
                j += 1
            else:
                return 0
        return abs_min % 2147483648
