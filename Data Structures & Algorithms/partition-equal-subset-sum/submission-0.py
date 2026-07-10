class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        totalSum = sum(nums)

        def dfs(i, curSum):
            if curSum == (totalSum - curSum):
                return True
            
            if i >= n:
                return False

            if dfs(i + 1, curSum + nums[i]) or dfs(i + 1, curSum):
                return True
            
            return False
        

        return dfs(0, 0)