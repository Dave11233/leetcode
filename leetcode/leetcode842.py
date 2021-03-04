class Solution:
    def splitIntoFibonacci(self, S: str):

        if len(S) < 3:
            return []
        for i in range(1, len(S)):
            sub_string1 = S[:i]
            if sub_string1 > 2**31-1:break

            if sub_string1.startswith("0") and sub_string1 != "0":
                break
            for j in range(i + 1, len(S)):
                sub_string2 = S[i:j]
                ans = [sub_string1, sub_string2]
                if sub_string2.startswith("0") and sub_string2 != "0":
                    break
                length = len(sub_string1) + len(sub_string2)
                sub_str1 = sub_string1
                sub_str2 = sub_string2
                while length <= len(S):
                    # if int(sub_string2) < int(sub_string1):
                    #     # print(sub_string1, sub_string2)
                    #     break
                    sub_str = int(sub_str1) + int(sub_str2)
                    sub_str = str(sub_str)

                    if not S[length:].startswith(sub_str):
                        break
                    sub_str1, sub_str2 = sub_str2, sub_str
                    length += len(sub_str)
                    ans.append(sub_str)
                if length == len(S):
                    print("".join(ans), S)
                    return [int(item) for item in ans]
        return []


if __name__ == '__main__':
    print(Solution().splitIntoFibonacci("123456579"))