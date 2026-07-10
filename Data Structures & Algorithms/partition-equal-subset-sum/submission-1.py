class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        totalSum = sum(nums)

        memo = {}
        def dfs(i, curSum):
            pair = (i, curSum)
            if pair in memo:
                return memo[pair]

            if curSum == (totalSum - curSum):
                memo[pair] = True
                return True
            
            if i >= n:
                memo[pair] = False
                return False

            if dfs(i + 1, curSum + nums[i]) or dfs(i + 1, curSum):
                memo[pair] = True
                return True
            
            memo[pair] = False
            return False
        

        return dfs(0, 0)