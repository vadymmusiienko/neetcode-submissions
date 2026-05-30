class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Construct a frequency map
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        # Bucket sort frequencies in reverse
        freqs = [[] for _ in range(len(nums))]

        for num, freq in freq_map.items():
            freqs[len(nums) - freq].append(num)
        
        # Find k-th frequent elem
        res = []
        for i in range(len(freqs)):
            for num in freqs[i]:
                res.append(num)
                if len(res) == k:
                    return res