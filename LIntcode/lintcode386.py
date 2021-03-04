from collections import defaultdict


class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        left = 0
        right = 0
        counter = defaultdict()
        res = 0
        while right < len(s):
            if s[right] in counter:
                counter[s[right]] += 1
                right += 1
            else:
                if len(counter) < k:
                    if s[right] in counter:
                        counter[s[right]] += 1
                    else:
                        counter[s[right]] = 1
                    right += 1
                else:
                    res = max(res, right - left)

                    counter[s[left]] -= 1
                    if counter[s[left]] == 0:
                        counter.pop(s[left])

                    left += 1

        res = max(res, right - left)
        return res


if __name__ == '__main__':
    print(
        Solution().lengthOfLongestSubstringKDistinct(
            "eceba", 3
        )
    )
