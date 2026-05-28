class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Compare Letter Frequencies
        s_freq = {}
        t_freq = {}
        for i in range(len(s)):
            s_freq[s[i]] = s_freq.get(s[i], 0) + 1
            t_freq[t[i]] = t_freq.get(t[i], 0) + 1

        return s_freq == t_freq
        

        