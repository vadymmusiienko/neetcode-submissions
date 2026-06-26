from collections import defaultdict
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        nums.sort(key=lambda x: (freqs[x], -x))
        return nums
        