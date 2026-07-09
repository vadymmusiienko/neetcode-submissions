class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        resLen, resIdx = 0, 0
        for center in range(n):
            # Odd palindrome
            left = right = center
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > resLen:
                    resLen = right - left + 1
                    resIdx = left
                
                left -= 1
                right += 1

            # Even palindrome
            left, right = center, center + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > resLen:
                    resLen = right - left + 1
                    resIdx = left
                
                left -= 1
                right += 1
        
        return s[resIdx : resIdx + resLen]
