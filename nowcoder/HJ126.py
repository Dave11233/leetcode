from typing import List


class Solution:
    def charSort(self, s:List[str]):
        if not s:
            return
        cache = {}
        for char in s:
            if char.isalpha():
                index = ord(char) - ord("A") if char.isupper() else ord(char) - ord('a')
                if index not in cache:
                    cache[index] = []
                cache[index].append(char)
        ans = ""
        for char in s:
            if not char.isalpha():
                ans += char
            else:
                while cache:
                    min_index = min(cache.keys())
                    queue = cache[min_index]
                    if queue:
                        add_char = queue.pop(0)
                        break
                    else:
                        cache.pop(min_index)
                ans += add_char

        return ans


if __name__ == '__main__':
    while True:
        try:
            s = input()
            s = list(s)
            # Solution().charSort(s)
            print(Solution().charSort(s))
        except:
            break
