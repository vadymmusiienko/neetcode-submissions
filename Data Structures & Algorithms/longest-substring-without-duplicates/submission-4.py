class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        longest = 0
        left = 0
        cur_letters = set(s[left])
        for right in range(1, len(s)):

            if s[right] in cur_letters:
                longest = max(longest, right - left)

                while s[right] in cur_letters:
                    cur_letters.remove(s[left])
                    left += 1
            
            cur_letters.add(s[right])
        
        longest = max(longest, right + 1 - left)
        return longest
            
        