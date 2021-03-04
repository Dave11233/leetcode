class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if S == "":
            return []
        ans = [""]
        for i in range(len(S)):
            temp_ans = []
            if S[i] in "0123456789":
                for a in ans:
                    temp_ans.append(a + S[i])
            else:
                for a in ans:
                    if S[i].isupper():
                        temp_ans.append(a+S[i])
                        temp_ans.append(a+S[i].lower())
                    else:
                        temp_ans.append(a + S[i])
                        temp_ans.append(a + S[i].upper())
            ans = temp_ans
        return ans
