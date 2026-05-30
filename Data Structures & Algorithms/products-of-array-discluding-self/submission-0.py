class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix sum
        left_prod = [1]
        for i in range(len(nums) - 1):
            left_prod.append(left_prod[i] * nums[i])
        
        # Suffix sum
        right_prod = [1]
        for i in range(len(nums) - 1, 0, -1):
            right_prod.append(right_prod[-1] * nums[i])
        right_prod.reverse()

        # Find the final array
        return [(left * right) for left, right in zip(left_prod, right_prod)]
        