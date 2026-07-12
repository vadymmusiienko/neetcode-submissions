class Solution:
    def hammingWeight(self, n: int) -> int:
        
        res = 0
        while n:
            mask = 0x1
            res += mask & n
            n = n >> 1
        
        return res