class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix sum
        res = [1] * len(nums)
        for i in range(len(nums) - 1):
            res[i + 1] = res[i] * nums[i]
        
        # Suffix sum
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res