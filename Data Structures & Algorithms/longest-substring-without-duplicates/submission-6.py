class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        longest = 0
        left = 0
        cur_letters = {}

        for right in range(len(s)):

            if s[right] in cur_letters:
                longest = max(longest, right - left)
                left = max(cur_letters[s[right]] + 1, left)

            
            cur_letters[s[right]] = right
        
        longest = max(longest, right + 1 - left)
        return longest
            
        