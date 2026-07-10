class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largestSum = nums[0]
        currSum = 0
        for num in nums:
            # Either start new or continue
            currSum = max(num, currSum + num)
            largestSum = max(largestSum, currSum)

        return largestSum