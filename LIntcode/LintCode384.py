class Solution:
    """
    @param s: a string
    @return: an integer
    """

    def lengthOfLongestSubstring(self, s: str):
        if not s:
            return 0
        left, right = 0, 0
        cache = {}
        count = 0
        ans = 0
        while left < len(s) and right < len(s):
            if s[right] not in cache:
                cache[s[right]] = 1
                count += 1
                ans = max(ans, count)
                right += 1
            else:
                # ans = max(ans, count)
                while s[right] in cache:
                    cache.pop(s[left])
                    left += 1
                    count -= 1
        return ans


