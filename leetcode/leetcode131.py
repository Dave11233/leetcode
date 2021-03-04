class Solution:
    def is_reverse(self, s):
        if not s:
            return True
        else:
            return s == s[::-1]

    def partition(self, s: str):
        if not s:
            return []
        ans = []
        length = len(s)

        def helper(start=0, temp_ans=[]):
            if start == length:
                ans.append(temp_ans)
            for i in range(start, length):
                if self.is_reverse(s[start:(i+1)]):
                    temp_ans.append(s[start:(i+1)])
                    temp_ans.pop()
                else:
                    continue
        helper()
        return ans
