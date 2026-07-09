class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        def centerPalindrome(left, right):
            nonlocal res
            while left >= 0 and right < n and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        
        for center in range(n):
            centerPalindrome(center, center)
            centerPalindrome(center, center + 1)
        
        return res
        
        