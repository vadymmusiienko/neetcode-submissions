class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        seen = set()

        res = 0
        for num in nums:
            if num in seen:
                continue

            streak, curr = 0, num
            while curr in nums_set:
                seen.add(curr)
                streak += 1
                curr += 1
            res = max(res, streak)
        return res

        