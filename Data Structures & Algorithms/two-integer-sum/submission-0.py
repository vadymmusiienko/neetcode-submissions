class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}

        for i in range(len(nums)):
            num = nums[i]

            if num in targets:
                return [targets[num], i]
            
            t = target - num
            if t not in targets:
                targets[t] = i
        
        return []
            
