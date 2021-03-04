class Solution:
    def subsetsWithDup(self, nums):
        """
        算法思想：每次增加增加内部的一个数据，由于是组合，将nums中的数据进行统计
        然后每次增加1至数字出现的次数次，然后不断的迭代
        :param nums:
        :return:
        """
        from collections import Counter
        counter = Counter(nums)
        res = [[]]
        for key, value in counter.items():
            temp_res = res.copy()
            for temp in res:
                temp_res.extend(temp + [key] * (i + 1) for i in range(value))
            res = temp_res
        return res
