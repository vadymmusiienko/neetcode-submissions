class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= k:
            return len(s)

        freqs = {}
        longest = 0

        left = 0
        maxf = 0 
        for right in range(len(s)):
            letter = s[right]

            freqs[letter] = freqs.get(letter, 0) + 1
            maxf = max(maxf, freqs[letter])

            while (right - left + 1) - maxf > k:
                freqs[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
        
        return longest
                
