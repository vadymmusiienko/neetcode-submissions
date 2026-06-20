class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(idx, target):
            if target == 0:
                # Done here
                res.append(subset.copy())
                return

            if idx >= len(nums):
                # Too far
                return

            if nums[idx] <= target:
                # Use
                subset.append(nums[idx])
                dfs(idx, target - nums[idx])
                subset.pop()

            # Skip
            dfs(idx + 1, target)

        
        dfs(0, target)
        return res