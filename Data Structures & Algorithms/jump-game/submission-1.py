class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n)
        dp[n - 1] = True
        for pos in range(n - 2, -1, -1):
            maxJ = nums[pos]
            for reachable in range(pos + 1, min(pos + 1 + maxJ, n)):
                if dp[reachable]:
                    dp[pos] = True
                    break

        return dp[0]
