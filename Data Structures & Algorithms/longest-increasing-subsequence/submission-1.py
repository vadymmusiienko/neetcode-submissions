class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {n : 0}
        def dfs(i, prev):
            if i >= n:
                return 0

            pair = (i, prev)
            if pair in memo:
                return memo[pair]
            
            curr = nums[i]
            if curr > prev:
                # Add or not
                memo[pair] = max(1 + dfs(i + 1, curr), dfs(i + 1, prev))
                return memo[pair]
            
            # Curr <= prev, so must skip
            memo[pair] = dfs(i + 1, prev)
            return memo[pair]

        
        return dfs(0, float("-inf"))