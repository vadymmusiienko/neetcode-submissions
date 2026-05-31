class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        res = 0
        for num in nums:
            if num - 1 in nums_set:
                continue
            
            # Start of the sequence
            streak, curr = 0, num
            while curr in nums_set:
                streak += 1
                curr += 1
            
            res = max(res, streak)

        return res

        