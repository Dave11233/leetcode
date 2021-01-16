class Solution:
    def subsets(self, nums):
        x = [[]]

        for i in nums:
            temp_list = []
            for y in x:
                temp_list.append(y+[i])
            x += temp_list.copy()

        return x

if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1,2,3]))