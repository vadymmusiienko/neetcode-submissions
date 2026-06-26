from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freqs = Counter(arr1)
        res = []
        end = []
        arr2_set = set(arr2)
        for num in arr2:
            for _ in range(freqs[num]):
                res.append(num)
        
            
        for num in arr1:
            if num not in arr2_set:
                end.append(num)
        
        end.sort()
        res.extend(end)
        return res