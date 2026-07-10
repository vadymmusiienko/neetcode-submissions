class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        n = len(nums)
        if totalSum % 2 == 1:
            return False
        
        target = totalSum // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for t in range(target, num - 1, -1):
                dp[t] = dp[t] or dp[t - num]

        return dp[target]
            
