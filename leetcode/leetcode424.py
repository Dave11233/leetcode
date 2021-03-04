class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        counter = [0] * 26 # 计算一个区间内出现的字母次数
        left = 0
        max_len = 0 # 存储一个区间内出现的最多的连续字母数

        for right, c in enumerate(s):
            counter[ord(c) - ord("A")] += 1
            max_len = max(max_len, counter[ord(c) - ord("A")])
            if right - left + 1 > max_len + k: # 当修改次数大于k次，滑动窗口移动
                counter[ord(s[left]) - ord("A")] -= 1 # 左边字母出现次数减1
                left += 1
        return len(s) - left
