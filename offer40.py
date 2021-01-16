class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if len(arr) <= 1:
            return arr
        else:
            dummy = arr[0]
            left = [item for item in arr if item <= dummy]
            right = [item for item in arr if item > dummy]
            low = self.getLeastNumbers(left[1:], k)
            high = self.getLeastNumbers(right, k)
            if len(low) >= k:
                return low[:k]
            else:
                return low + [dummy] + high[:(k - len(low) - 1)]