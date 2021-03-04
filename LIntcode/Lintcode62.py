class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """

    def search(self, A: list, target: int):
        if not A:
            return -1
        left, right = 0, len(A) - 1
        while left <= right:
            mid = left + (right - left) >> 1
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                right = mid - 1

            else:
                if A[left] < target:
                    right = mid - 1
                elif A[right] > target:
                    left = mid + 1
        return -1
