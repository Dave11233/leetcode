class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """

    def minWindow(self, source, target):
        # write your code here
        if len(source) <= 0 or len(target) <= 0:
            return ""

        matchedHash = {}
        targetHash = {}
        for char in target:
            targetHash[char] = (1 if targetHash.get(char) == None else targetHash.get(char) + 1)

        targetUniqueLen = len(targetHash)
        matchedUniqueLen = 0

        minLen = len(source) + 1
        minString = ""

        j = 0

        for i in range(len(source)):
            while j < len(source) and matchedUniqueLen < targetUniqueLen:
                if source[j] in targetHash:
                    matchedHash[source[j]] = (
                        1 if matchedHash.get(source[j]) is None else matchedHash.get(source[j]) + 1)
                    if matchedHash[source[j]] == targetHash[source[j]]:
                        matchedUniqueLen += 1
                j += 1

            if j - i < minLen and matchedUniqueLen == targetUniqueLen:
                minLen = j - i
                minString = source[i:j]

            if source[i] in targetHash:
                if matchedHash[source[i]] == targetHash[source[i]]:
                    matchedUniqueLen -= 1

                matchedHash[source[i]] -= 1

        return minString


if __name__ == '__main__':
    print(
        Solution().minWindow(
            "aaaaaaaaaaaabbbbbcdd", "abcdd"
        )
    )
