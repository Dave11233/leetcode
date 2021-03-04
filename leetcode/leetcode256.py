class Solution:
    def countArrangement(self, n: int) -> int:
        if n == 0:
            return 0
        self.count = 0

        def helper(cur_location=1, temp_ans=[]):
            if cur_location == n + 1:
                self.count += 1

                return
            for i in range(1, n + 1):
                if i not in temp_ans and (cur_location % i == 0 or i % cur_location == 0):
                    temp_ans.append(i)
                    helper(cur_location + 1, temp_ans)
                    temp_ans.pop()

        helper()
        return self.count

if __name__ == '__main__':
    print(Solution().countArrangement(3))
