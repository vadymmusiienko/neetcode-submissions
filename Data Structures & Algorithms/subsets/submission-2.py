class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(len(nums)):
            subset = [s + [nums[i]] for s in res]
            res.extend(subset)
        return res
