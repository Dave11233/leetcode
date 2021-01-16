class Solution:
    def combinationSum2(self, candidates, target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []
        def helper(candidates, target, index):
            if target == 0:
                res.append(path.copy())
                return
            else:
                for i in range(index, len(candidates)):
                    if candidates[i] <= target:
                        if i > index and candidates[i] == candidates[i - 1]:
                            continue
                        path.append(candidates[i])
                        helper(candidates, target - candidates[i], i + 1)
                        path.pop()
        helper(candidates, target, 0)
        return res