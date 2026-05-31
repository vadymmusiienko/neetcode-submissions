class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def twoSum(i, left, right, target):
            while left < right:
                curr_sum = nums[left] + nums[right]

                if curr_sum > target:
                    right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    prev = nums[left]
                    res.append([nums[i], prev, nums[right]])
                    
                    while left < right and prev == nums[left]:
                        left += 1
        
        prev = None
        for left in range(len(nums) - 2):
            if nums[left] == prev:
                continue
            target = -nums[left]
            twoSum(left, left + 1, len(nums) - 1, target)
            prev = nums[left]
                
        
        return res



        
