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
        i = 0
        res = []
        while k > 0 and i < len(freqs):
            j = 0
            while k > 0 and j < len(freqs[i]):
                res.append(freqs[i][j])
                k -= 1
                j += 1
                
            i += 1
        

        print(freqs)
        print(freq_map)
        return res
            
