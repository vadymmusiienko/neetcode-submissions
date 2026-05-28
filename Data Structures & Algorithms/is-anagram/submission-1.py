class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letter_freq = [0] * 26
        for i in range(len(s)):
            letter_freq[ord(s[i]) - ord('a')] += 1
            letter_freq[ord(t[i]) - ord('a')] -= 1
        
        for freq in letter_freq:
            if freq != 0:
                return False
        
        return True


        

        