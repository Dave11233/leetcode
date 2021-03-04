class Solution:
    def solve(self, s: str):
        if not s:
            return ""
        from collections import Counter
        hash_map = Counter(s)
        x = sorted(zip(hash_map.keys(), hash_map.values()), key=lambda x: x[1])
        temp_dict = {}
        ans = ""
        for i in x:
            if i[1] not in temp_dict:
                temp_dict[i[1]] = []
            temp_dict[i[1]].append(i[0])
        for key, values in temp_dict.items():
            values.sort()
            ans += "".join(values)
        return ans


if __name__ == '__main__':
    S = input()
    print(Solution().solve(S))
