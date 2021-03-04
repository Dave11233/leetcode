from typing import List


class Solution:
    def charSort(self, l: List[str]) -> List[str]:
        if not l:
            return []
        l.sort()
        return l


if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())
