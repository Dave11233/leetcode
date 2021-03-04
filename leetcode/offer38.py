class Solution:
    def permutation(self, s: str):
        ans = []

        def helper(string=s, temp_s=""):
            if string == "":
                if temp_s not in ans:
                    ans.append(temp_s)
                return
            else:
                for i in range(len(string)):
                    x = string[i]
                    helper(string[:i] + string[(i + 1):], temp_s + x)

        helper()
        return ans


if __name__ == '__main__':
    print(Solution().permutation("ryawrowv"))
