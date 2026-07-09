class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        def centerPalindrome(left, right):
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            
            return count
            
        
        for center in range(n):
            res += centerPalindrome(center, center)
            res += centerPalindrome(center, center + 1)
        
        return res
        
        