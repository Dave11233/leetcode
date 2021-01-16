class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        if target < 0:
            return []
        res = []

        def helper(cur_sum=0, temp=[], location=0):
            if cur_sum > target:
                return
            if cur_sum == target:
                res.append(temp.copy())
                return
            for i in range(len(candidates)):
                if location <= i:
                    temp += [candidates[i]]
                    helper(cur_sum + candidates[i], temp, i)
                    temp.pop()

        helper()
        return list(res)
