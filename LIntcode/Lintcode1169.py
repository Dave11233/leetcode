class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: if s2 contains the permutation of s1
    """
    def checkInclusion(self, s1, s2):

        if s1 == "":
            return True
        if s2 == "" and len(s1) > 0:
            return False

        s1_counter = {}
        for char in s1:
            if char not in s1_counter:
                s1_counter[char] = 0
            s1_counter[char] += 1

        def helper(counter):
            for item in s1_counter:
                if item in counter:
                    if counter[item] != s1_counter[item]:
                        return False
                else:
                    return False
            return True
        temp_counter = {}
        left = 0
        right = 0
        while right < len(s2):

            if s2[right] in s1_counter:
                if s2[right] not in temp_counter:
                    temp_counter[s2[right]] = 0
                temp_counter[s2[right]] += 1
                while s1_counter[s2[right]] < temp_counter[s2[right]]:
                    temp_counter[s2[left]] -= 1
                    left += 1
                if helper(temp_counter):
                    return True
                right += 1
            else:
                temp_counter = {}
                right += 1
                left = right

        return False


if __name__ == '__main__':
    print(
        Solution().checkInclusion(
            'qrcczceam',
            'xxyhdqrloraznjmjdutowpdihgojmpkbhytwkplsqolieeinuedffiqrlkgcljktvyppfztcuyoinzfntyjnmjvwwwmatbbfsriwrwonesmcmcdamurgovwlvssposzrjeiexpdcojeqhjxbpoaecqibkybyrjxqibmnybdmizrmrzzwsojfsmyfgvmyscwgaotnjlfwnixdyxlxhtuwwrkcsefubrfxlexixuerldgsuuklrsvrhqndbmslrrtqsudjsgseohbwgojjmepfsawhszluynmfvlfosihatyvupzkxukiedwgmpxsznaqadvalzmigsitmwaunstoqlgskhnsmwvrudgphbnn'
        )
    )
