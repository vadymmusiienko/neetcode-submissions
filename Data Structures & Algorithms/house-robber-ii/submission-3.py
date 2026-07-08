class Solution:
    def rob(self, nums: List[int]) -> int:

        def robOne(houses):
            if not houses:
                return 0
            if len(houses) == 1:
                return houses[0]

            dp0 = houses[0]
            dp1 = max(dp0, houses[1])
            for i in range(2, len(houses)):
                tmp = max(dp1, dp0 + houses[i])
                dp0 = dp1
                dp1 = tmp
            
            return dp1
        
        n = len(nums)
        if n == 1:
            return nums[0]
        first = nums[0:n-1]
        second = nums[1:]


        return max(robOne(first), robOne(second))
        
        
        