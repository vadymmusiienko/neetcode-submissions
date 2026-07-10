class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        currMax = currMin = 1
        maxGlobal = nums[0]
        for i in range(n):
            curr = nums[i]
            tmp = currMax * curr
            currMax = max(curr, tmp , currMin * curr)
            currMin = min(curr, currMin * curr, tmp)
            maxGlobal = max(maxGlobal, currMax)
        
        return maxGlobal