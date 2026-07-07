class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp0 = nums[0]
        dp1 = max(nums[0], nums[1])

        for i in range(2, n):
            if i % 2 == 0:
                dp0 = max(dp0 + nums[i], dp1)
            else:
                dp1 = max(dp1 + nums[i], dp0)
        
        return max(dp1, dp0)