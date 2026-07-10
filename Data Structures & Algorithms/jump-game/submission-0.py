class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {n-1: True}

        def dfs(pos):
            if pos in memo:
                return memo[pos]
            
            if pos >= n:
                return False
            
            maxJ = nums[pos]
            for j in range(maxJ, 0, -1):
                memo[pos] = dfs(pos + j)
                if memo[pos]:
                    return True
            
            memo[pos] = False
            return False
        
        return dfs(0)
