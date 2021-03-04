class Solution:

    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        if all([i == "0" for i in num]):
            return True
        if not num:
            return False

        for i in range(1, len(num)):
            sub_string1 = num[:i]
            if sub_string1.startswith("0") and sub_string1 != "0":
                break
            for j in range(i + 1, len(num)):
                sub_string2 = num[i:j]
                if sub_string2.startswith("0") and sub_string2 != "0":
                    break
                length = len(sub_string2) + len(sub_string1)
                s_string1 = sub_string1
                s_string2 = sub_string2
                while length <= len(num):
                    s_string3 = int(s_string2) + int(s_string1)
                    s_string3 = str(s_string3)
                    sub_string = num[length:]
                    if not sub_string.startswith(s_string3):
                        break
                    length += len(s_string3)
                    s_string2, s_string1 = s_string3, s_string2
                if length == len(num):
                    return True

        return False


if __name__ == '__main__':
    solution = Solution()
    num = "121224036"
    print(solution.isAdditiveNumber(num))
