class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            raise ValueError("There is forbidden in the string with empty")
        list_str = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        res = list_str[digits[0]]
        for item in digits[1:]:
            temp = res.copy()
            z = list_str[item]
            j = []
            for x in temp:
                for t in z:
                    j.append(x + t)
            res = j.copy()
        return res

