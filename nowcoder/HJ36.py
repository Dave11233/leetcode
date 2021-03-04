class Solution:
    def helper(self, key_dict:dict, s:str):
        ans = ""
        for i in s:
            if i.isupper():
                ans += key_dict[i]
            else:
                ans += key_dict[i.upper()].lower()
        return ans

    def solve(self, key: str, s: str) -> str:
        if not key:
            return s
        if not s:
            return ""
        key = key.upper()
        # s = s.upper()
        # ans = ""
        been_key = set()
        index = ord("A")
        public_key = {}
        for i in key:
            if i not in been_key:
                been_key.add(i)
                public_key[i] = chr(index)
                # print(i,  chr(index))
                index += 1
        # print("index", index)
        # if len(public_key) == 26:
        #     return self.helper(public_key, s)
        other_index = ord("A")
        for i in range(index, ord("Z")+1):
            # print(chr(other_index))
            while chr(other_index) in been_key:
                other_index += 1

            public_key[chr(other_index)] = chr(i)
            been_key.add(chr(other_index))
        # print(public_key)
        # print(len(been_key))
        public_key = dict(zip(public_key.values(), public_key.keys()))

        return self.helper(public_key, s)


if __name__ == '__main__':
    while True:
        try:
            key = input()
            s = input()
            print(Solution().solve(key, s))
        except EOFError:
            break