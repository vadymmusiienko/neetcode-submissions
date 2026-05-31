class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def twoSum(first, left, right, target):
            while left < right:
                curr_sum = nums[left] + nums[right]

                if curr_sum > target:
                    right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    res.append([first, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
        for idx, num in enumerate(nums):
            # Since sorted, no more triplets for pos numbers
            if num > 0:
                break 
            
            # Skip duplicates
            if idx > 0 and num == nums[idx - 1]:
                continue
            
            twoSum(nums[idx], idx + 1, len(nums) - 1, -nums[idx])
        
                
        
        return res



        
