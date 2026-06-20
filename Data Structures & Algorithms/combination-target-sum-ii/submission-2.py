class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []
        candidates.sort()
        def dfs(idx, target):
            if target == 0:
                res.append(subset.copy())
                return

            if idx >= len(candidates) or candidates[idx] > target:
                return
            
            if candidates[idx] <= target:
                subset.append(candidates[idx])
                dfs(idx + 1, target - candidates[idx])
                subset.pop()
            
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            
            dfs(idx + 1, target)
        
        dfs(0, target)
        return res
                