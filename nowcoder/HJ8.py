class Solution:
    def mergeKeyValueAndSort(self, hashMap:dict):
        if not hashMap:
            return {}
        return dict(sorted(zip(hashMap.keys(), hashMap.values()), key=lambda x:x[0]))


if __name__ == '__main__':
    n = int(input())
    hashMap = {}
    for _ in range(n):
        s = input()
        key, value = s.split(" ")
        key = int(key)
        value = int(value)
        if key not in hashMap:
            hashMap[key] = value
        else:
            hashMap[key] += value
    result = Solution().mergeKeyValueAndSort(hashMap)
    for key, value in result.items():
        print(key, "\t", value)