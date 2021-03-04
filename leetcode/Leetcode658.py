class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr:
            return []
        arr.sort(key=lambda t: abs(x - t))
        return arr[:k]
